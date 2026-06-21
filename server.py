import os
import random
import time
import logging
import requests
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from yoto_api import YotoClient, Token

from stories import STORIES

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

import yoto_api.auth as _yoto_auth_module
from yoto_api.exceptions import YotoAPIError as _YotoAPIError

_original_build_token = _yoto_auth_module._build_token


def _patched_build_token(body, scope, prev_refresh=None):
    if "refresh_token" not in body and prev_refresh is not None:
        body = {**body, "refresh_token": prev_refresh}
    return _original_build_token(body, scope)


def _patched_refresh(self_auth, token):
    async def _inner():
        import aiohttp

        data = {
            "client_id": self_auth.client_id,
            "grant_type": "refresh_token",
            "refresh_token": token.refresh_token,
            "audience": "https://api.yotoplay.com",
        }
        try:
            async with self_auth._session.post(
                "https://login.yotoplay.com/oauth/token",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            ) as response:
                resp_body = await response.json(content_type=None)
        except Exception as err:
            raise _YotoAPIError(f"Refresh token request failed: {err}") from err
        if resp_body.get("error"):
            from yoto_api.exceptions import AuthenticationError

            raise AuthenticationError("Refresh token invalid")
        return _patched_build_token(
            resp_body, scope=token.scope, prev_refresh=token.refresh_token
        )

    return _inner()


_yoto_auth_module.Auth.refresh = _patched_refresh

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID            = os.getenv("YOTO_VOICE_ID_STORY")
ELEVENLABS_URL      = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

YOTO_CLIENT_ID     = os.getenv("YOTO_CLIENT_ID")
YOTO_REFRESH_TOKEN = os.getenv("YOTO_REFRESH_TOKEN")
YOTO_DEVICE_ID     = os.getenv("YOTO_DEVICE_ID")
YOTO_CARD_ID       = os.getenv("YOTO_CARD_ID")

MAX_DEPTH = 5

CHAPTER_STORY  = "02"
TRACK_LEFT     = "01"
TRACK_PROMPT   = "02"
TRACK_RIGHT    = "03"

CHAPTER_ENDING = "03"
TRACK_ENDING   = "01"

sessions: dict[str, dict] = {}
yoto_client: YotoClient | None = None
_last_seen_track: dict[str, tuple] = {}


def get_session(player_id: str) -> dict:
    return sessions.get(player_id)


def new_session(player_id: str) -> dict:
    story = random.choice(STORIES)
    session = {
        "story":          story,
        "node_key":       "1",
        "depth":          0,
        "ended":          False,
        "started":        time.time(),
        "pending_text":   None,
        "passage_read":   False,
    }
    sessions[player_id] = session
    log.info(f"New session: player={player_id} story='{story['title']}'")
    return session


def current_node(session: dict) -> dict:
    return session["story"]["nodes"][session["node_key"]]


def tts_stream(text: str):
    log.info(f"TTS ({len(text)} chars): {text[:80]}...")
    resp = requests.post(
        ELEVENLABS_URL,
        headers={"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"},
        json={
            "text": text,
            "model_id": "eleven_turbo_v2",
            "voice_settings": {"stability": 0.55, "similarity_boost": 0.75},
        },
        stream=True,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.iter_content(chunk_size=4096)


def audio(text: str) -> StreamingResponse:
    return StreamingResponse(tts_stream(text), media_type="audio/mpeg")


def player_id_from_request(request: Request) -> str:
    return (
        request.headers.get("x-yoto-device-id")
        or request.headers.get("x-device-id")
        or YOTO_DEVICE_ID
        or request.client.host
        or "default"
    )


def choice_prompt(node: dict) -> str:
    return (
        f"Turn the right knob forward to {node['left']}. "
        f"Or turn it back to {node['right']}."
    )


def _advance_node(session: dict, direction: str) -> str:
    """Move to the next node based on direction, return narration text."""
    node = current_node(session)

    if node.get("ending"):
        return "Your adventure is already complete!"

    next_key = node.get(f"{direction}_node")
    if not next_key:
        return "I couldn't find that path through the jungle."

    session["node_key"] = next_key
    session["depth"]   += 1
    session["passage_read"] = False

    next_node = current_node(session)
    chosen_action = node["left"] if direction == "left" else node["right"]
    ack = f"You chose to {chosen_action.lower()}. "

    if next_node.get("ending"):
        session["ended"] = True
        return f"{ack}{next_node['text']} Turn the right knob forward to finish your adventure!"
    else:
        return f"{ack}{next_node['text']} {choice_prompt(next_node)}"


async def _on_player_update(player) -> None:
    event = player.last_event
    if event is None:
        return

    device_id   = event.player_id
    chapter_key = event.chapter_key
    track_key   = event.track_key

    log.info(
        f"[MQTT EVENT] device={device_id} chapter_key={chapter_key!r} "
        f"track_key={track_key!r} playback_status={event.playback_status!r}"
    )

    if chapter_key is None or track_key is None:
        return
    if chapter_key != CHAPTER_STORY:
        return
    if track_key not in (TRACK_LEFT, TRACK_RIGHT):
        return

    pid = device_id
    session = get_session(pid)
    if not session:
        log.warning(f"Landing event for {pid} with no active session, ignoring")
        return

    dedup_signal = (chapter_key, track_key, event.event_utc, event.request_id)
    if _last_seen_track.get(device_id) == dedup_signal:
        return
    _last_seen_track[device_id] = dedup_signal

    direction = "left" if track_key == TRACK_LEFT else "right"
    log.info(f"Player {pid} turned {direction}")

    narration = _advance_node(session, direction)
    session["pending_text"] = narration

    node = current_node(session)
    try:
        if node.get("ending"):
            await yoto_client.play_card(
                device_id, YOTO_CARD_ID,
                chapter_key=CHAPTER_STORY, track_key=TRACK_PROMPT,
            )
        else:
            await yoto_client.play_card(
                device_id, YOTO_CARD_ID,
                chapter_key=CHAPTER_STORY, track_key=TRACK_PROMPT,
            )
    except Exception:
        log.exception(f"Failed to redirect player {pid} after choice")


async def _start_mqtt():
    global yoto_client
    if not (YOTO_CLIENT_ID and YOTO_REFRESH_TOKEN and YOTO_DEVICE_ID):
        log.warning(
            "YOTO_CLIENT_ID / YOTO_REFRESH_TOKEN / YOTO_DEVICE_ID not all set "
            "- MQTT branching is disabled. Audio will still stream, but choices won't be detected."
        )
        return
    if not YOTO_CARD_ID:
        log.warning("YOTO_CARD_ID not set - MQTT branching is disabled until configured.")
        return

    client = None
    try:
        client = YotoClient(client_id=YOTO_CLIENT_ID)
        client.set_refresh_token(YOTO_REFRESH_TOKEN)
        await client.check_and_refresh_token()
        await client.update_player_list()

        if YOTO_DEVICE_ID not in client.players:
            log.warning(
                f"YOTO_DEVICE_ID {YOTO_DEVICE_ID} not found in account's device list "
                f"({list(client.players)}) - check the ID is correct."
            )

        yoto_client = client
        await yoto_client.connect_events([YOTO_DEVICE_ID], on_update=_on_player_update)
        log.info(f"MQTT connected for device {YOTO_DEVICE_ID}")
    except Exception:
        log.exception("Failed to start MQTT - branching will be disabled, audio streaming still works.")
        if client is not None:
            try:
                await client.close()
            except Exception:
                pass
        yoto_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    await _start_mqtt()
    yield
    if yoto_client is not None:
        try:
            await yoto_client.disconnect_events()
        except Exception:
            log.exception("Error disconnecting MQTT on shutdown")


app = FastAPI(title="Yoto Adventure Server", lifespan=lifespan)


@app.get("/welcome")
async def welcome(request: Request):
    pid = player_id_from_request(request)
    session = new_session(pid)
    _last_seen_track.pop(pid, None)

    story = session["story"]
    text = (
        f"Welcome to Jungle Adventure! Today's story is: {story['title']}. "
        f"{story['intro']} Turn the right knob forward when you're ready to begin!"
    )
    return audio(text)


@app.get("/story")
async def story(request: Request):
    pid = player_id_from_request(request)
    session = get_session(pid)
    if not session:
        session = new_session(pid)

    pending = session.pop("pending_text", None)
    if pending:
        session["passage_read"] = True
        return audio(pending)

    node = current_node(session)
    session["passage_read"] = True

    if node.get("ending"):
        return audio(f"{node['text']} Turn the right knob forward to hear how your adventure ends!")

    remaining = MAX_DEPTH - session["depth"]
    if remaining == 1:
        hint = "This is your last choice - make it count!"
    elif remaining == 2:
        hint = "You are nearly at the end of your adventure."
    else:
        hint = ""

    text = f"{node['text']} {hint} {choice_prompt(node)}".strip()
    return audio(text)


@app.get("/left")
async def left_placeholder(request: Request):
    return audio(" ")


@app.get("/right")
async def right_placeholder(request: Request):
    return audio(" ")


@app.get("/ending")
async def ending(request: Request):
    pid = player_id_from_request(request)
    session = get_session(pid)

    if not session:
        return audio("Insert the card again to start a brand new jungle adventure!")

    node = current_node(session)
    if node.get("ending"):
        ending_type = node.get("ending_type", "triumph")
        if ending_type == "triumph":
            outro = "What an amazing adventure! You should be very proud. Insert the card again for a brand new story!"
        elif ending_type == "mishap":
            outro = "Things didn't go quite to plan - but that's what makes a great story! Try again for a different ending!"
        else:
            outro = "What a wonderfully unexpected adventure! The jungle is full of surprises. Insert the card again to discover another!"
        text = f"{node['text']} {outro}"
    else:
        text = "Your adventure isn't finished yet - go back and keep making choices!"

    sessions.pop(pid, None)
    _last_seen_track.pop(pid, None)
    return audio(text)


@app.get("/health")
async def health():
    return {
        "status":          "ok",
        "stories":         len(STORIES),
        "active_sessions": len(sessions),
        "mqtt_connected":  yoto_client is not None,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)