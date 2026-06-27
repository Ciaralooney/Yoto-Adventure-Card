"""
Story bank for Yoto Jungle Adventure.

Each story is a tree of nodes. Every node has:
  - text: the narration played at this point
  - left: text describing the left choice
  - right: text describing the right choice
  - left_node / right_node: the key of the next node
  - OR ending: True (leaf node, story ends here)
  - ending_type: "triumph" | "mishap" | "surprise"
    (used to pick the right tone for the ending music cue)

Nodes are keyed as strings. Root is always "1".
A tree with 5 decision points has nodes at depths 1–5,
with 16 leaf (ending) nodes.

For readability each story is written as a flat dict.
Keys follow a binary path: "1" -> "1L"/"1R" -> "1LL"/"1LR"/"1RL"/"1RR" etc.
"""

STORIES = [
    # STORY 1: The Lost Baby Elephant
    {
        "title": "The Lost Baby Elephant",
        "intro": (
            "It's early morning and you awake in your jungle home. You could have slept more but your heard something in the distance that was"
            " worrying you. As you walk down a muddy trail you begin to hear it more clearly. It sounds like a sad trumpeting. You look down "
            "to find a tiny baby elephant sitting alone with it's eyes full of tears."
        ),
        "nodes": {
            "1": {
                "text": (
                    "The elephant looks up to you hopefully. "
                    "Ahead you can see two trails. On one trail there is fresh elephant tracks leading toward a glittering river."
                    "The second trail leads further into the jungle and you can hear a distant rumbling at the end of the trail."
                    "Press the left button to Follow the tracks to the river. Press the right button to head toward the rumbling sound"
                ),
                "left": "Follow the tracks to the river",
                "right": "Head toward the rumbling sound",
                "left_node": "1L",
                "right_node": "1R",
            },

            # LEFT BRANCH: River path 
            "1L": {
                "text": (
                    "The baby elephant happily follows you as you walk along muddy tracks towards to the river. "
                    "At the water's edge you can see some beautiful colourful birds singing in the distance. They seem to be calling you over. "
                    "But in the distance you can just make out a large shape moving on a sandbar downstream (right)."
                    "Press the left button to Go upstream toward the birds. Press the right button to Head downstream to the sandbar"
                ),
                "left": "Go upstream toward the birds",
                "right": "Head downstream to the sandbar",
                "left_node": "1LL",
                "right_node": "1LR",
            },
            "1LL": {
                "text": (
                    "The birds are dleighted to see you. They are a bit surprised to see a baby elephant running behid you though. But the birds part ways to show you a hidden waterfall. The baby elephant goes to drink some water and then disapears. You panic just for moment until you realise he has ran behind the waterfall. You follow him to see the entrance of a dark cave. "
                    "Press the left button to Explore inside the cave. Press the right button to Wait and listen by the waterfall"
                ),
                "left": "Explore inside the cave",
                "right": "Wait and listen by the waterfall",
                "left_node": "1LLL",
                "right_node": "1LLR",
            },
            "1LLL": {
                "text": (
                    "You both walk inide the cave. The elephant runs ahead excitely. You stop for a moment and take in the ancient elephant carvings on the walls. You pull the baby elephant back as you see the cave gets deeper and narrower. "
                    "You stay a moment looking at the tunnel. The baby elephant tugs the player's sleeve urgently looking excited. "
                     "Press the left button to Follow the tunnel. Press the right button to Head back outside"
                ),
                "left": "Follow the tunnel",
                "right": "Head back outside",
                "left_node": "1LLLL",
                "right_node": "1LLLR",
            },
            "1LLLL": {
                "text": (
                    "You decide to follow the tunnel. You go through with the baby elephant in hand. He squirms impatiently as you navigate the dark terrain."
                    "But soon the tunnel opens into a beautiful hidden valley where the whole elephant herd "
                    "splashes in a pool. You set the baby elephant down and watch it charge towards its mother happily. "
                    "The mother wraps her trunk gently around you in thanks. It seems you have found the most secret place in the entire jungle."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLLR": {
                "text": (
                    "You leave the cave and go back outside. It just doesn't seem safe in there. You notice a large parrot eyeing you up. He swoops down and lands on your shoulder. In a squeaky voice he begins to give you directions."
                    "It says the herd is east of the old fig tree. You know where the fig tree is so you follow the directions and see an anxious herd of elephants. They seem much happier as the baby elephant charges towards them. They're very grateful to you for bringing theur baby home."
                    "and the baby safely returned home."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLR": {
                "text": (
                    "As you sit by the waterfall, a family of otters approches you"
                    "and to your amazement "
                    "they seem to understand your problem. "
                    "They dive and resurface, they're trying to lead you along the river. But should you follow them? . "
                    "Press the left button to Follow the otters. Press the right button to Find your own way"
                ),
                "left": "Follow the otters",
                "right": "Find your own way",
                "left_node": "1LLRL",
                "right_node": "1LLRR",
            },
            "1LLRL": {
                "text": (
                    "The otters lead you straight to a shallow crossing where the elephant herd was getting a drink. "
                    "the baby elephant waddles through the water. It almost completely covers him but he is determined to cross this shallow stream to reunite with his family. Suddently he is scooped up by his mother's trunk "
                    "The otters chitter happily as they swim away. The elephant look eternally grateful to you."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLRR": {
                "text": (
                    "Mishap ending: You try to make your way along but end up walking in circles since everyhting looks the same around here. As darkness falls you decide to setup a camp for the night. "
                    "You make a temporary shelter for yourself but as you turn around the baby elephant has climbed into it and dozed off. Oh well. You gather some banana leaves and sleep on those instead.  "
                    "In the morning you awake to several elephants watching you. It seems the herd was out searching all night and found you instead. Even if everyone is tired it's a very happy reunion"
                ),
                "ending": True,
                "ending_type": "mishap",
            },
            "1LR": {
                "text": (
                    "The sandbar is covered in large elephant footprints. They must have been here at some stage but the herd has moved on. The baby elephant trumpets sadly. "
                    "You can see a crocodile sleeping nearby, blocking the path. "
                    "You could try to sneak past the crocodile very quietly "
                    "or wade through the water instead."
                    "Press the left button to Sneak past the crocodile. Press the right button to Wade through the water"
                ),
                "left": "Sneak past the crocodile",
                "right": "Wade through the water",
                "left_node": "1LRL",
                "right_node": "1LRR",
            },
            "1LRL": {
                "text": (
                    "You pick up the baby elephant with great difficulty and tiptoe so carefully that even the baby elephant holds its breath."
                    "The crocodile continues to sleep "
                    "Beyond the sandbar you climb a tall hill and spot the herd below in a valley. "
                    "You both run down. You watch as the baby elephant sprints towards its mother, you smile as you wave at the trumpeting, delighted family!"
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LRR": {
                "text": (
                    "You begin to wade in the water but the baby elephant dissapears! You reach in and pull him out. The water here is far deeper than it looked. "
                    "You wade through holding the squirming baby elephant until you reach the other side. You sit down exhausted. You are soaking wet but  the baby elephant thinks this is hilarious and even goes back to the river bank to get water in its trunk to spray you with."
                    "All of this commotion alerts a passing monkey. The elephant seems to recognise the monkey and now both of them throwing water at you. After they had their fun they begin to amble together. You're still concerned so you follow them. The monkey led both of you to an opening where the elephant herd was. The baby elephant runs towards its mother and the elephants look at you very grateful. They know you went through a lot"
                ),
                "ending": True,
                "ending_type": "mishap",
            },

            # RIGHT BRANCH: Deep jungle rumbling 
            "1R": {
                "text": (
                    "You push through the thick plants toward the rumbling. It get's louder before stopping entirely. "
                    "You emerge into a clearing with an ancient tree at the centre. The tree must be the tallest one in the jungle."
                    "Press the left button to climb the tree for a bird's-eye view of the jungle. "
                    "or Press the right button to search around the roots where something might to be hiding."
                ),
                "left": "Climb the tree",
                "right": "Search around the roots",
                "left_node": "1RL",
                "right_node": "1RR",
            },
            "1RL": {
                "text": (
                    "You slowly inch up the tree. The baby elephant waits impatiently below. When you are halfway up you take a break and decide to look from here. You can see a sweeping view for miles. There are 2 landmarks in the distance. "
                    "You can see a red dust cloud and a herd of animals to the north and ranger station to the south. "
                    "Press the left button to go towards the dust cloud. Press the right button to go to the ranger station."
                ),
                "left": "Head north toward the dust cloud",
                "right": "Head south to the ranger station",
                "left_node": "1RLL",
                "right_node": "1RLR",
            },
            "1RLL": {
                "text": (
                    "You decide to run north through the herd. The baby elephant runs ahead. As you get closer you can see the huge dust cloud is from dozens of fast moving elephants. The baby elephant stands close to you."
                    "Press the left button to call out loudly to try slow the herd"
                    "Press the right button to find a way to get ahead of the herd"
                ),
                "left": "Call out loudly",
                "right": "Race ahead of the herd",
                "left_node": "1RLLL",
                "right_node": "1RLLR",
            },
            "1RLLL": {
                "text": (
                    "You shout as loud as you can. The baby elephant tries to help by trumpeting while jumping up and down. The herd slows. "
                    "The biggest elephant approches you and studies you slowly but when she sees the baby she lets out a thunderous trumpet call and so does the baby elephant "
                    "The whole herd gathers in a joyful huddle around the baby elephant. Well done, you brought the baby elephant home."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLLR": {
                "text": (
                    "You sprint through the undergrowth and with the help of a shortcut manage to get ahead. "
                    "You stand with the baby elephant in the path of the others and wait. They begin to slow down and the lead elephant sniffes the baby, You can see recognition dawning on her face. "
                    "She lets out a thunderous trumpet call and the baby elephant joins in. The whole herd gathers in a circle around the baby elephant. Your brave move paid off and you got the baby elephant home."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLR": {
                "text": (
                    "The ranger station door is unlocked and you walk in. A woman called Maya greets you and isn't too surprised to see a baby elephant with you. Apparently he's always wandering off. Maya knows exactly which herd the baby belongs to"
                    "and drives the you there in her jeep. Or that was the plan until the jeep gets a flat tyre halfway there. Maya says help won't be long arriving but it's getting dark."
                    "Press the left button to wait for help to arrive or Press the right button to walk the rest of the way."
                ),
                "left": "Wait for help",
                "right": "Walk the rest of the way",
                "left_node": "1RLRL",
                "right_node": "1RLRR",
            },
            "1RLRL": {
                "text": (
                    "Maya was right. Another ranger arrives just 10 minutes later to fix the tyre. In that time the baby elephant found a packet of peanuts in the jeep and helped himself."
                    "You reach the herd just before sunset. The mother of the elephant looks relieved as her baby runs towards here. You are so happy you could reunite them."
                    "To celebrate the occasion the baby elephant splashes into a muddy waterhole to celebrate which completely covers you and Maya in mud. But it was worth it."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLRR": {
                "text": (
                    "Walking through the jungle at dusk is spooky but magical. It's dark but fireflys light the way. The baby elephant clings to you. You realise even baby elephants are scared of the dark. "
                    "Maya gave you directions to where the heard would be. She was coreect too, it was just a short walk down a winding path. By the time you arrive the herd is settling in for the night. The baby elephant runs for his mother and his mother pulls him into her. "
                    "The mother and baby sleep curled together under the stars. You are content but exhaused so you deicde to sleep near the herd for tonight."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RR": {
                "text": (
                    "You carefully inspect the tree roots when all of a sudden a monkey steals the your hat and scampers up the tree. "
                    "The baby elephant laughs. The monkey wants you to follow it. "
                    "Press the left button to chase the monkey up the tree or Press the right button to ignore it."
                ),
                "left": "Chase the monkey up the tree",
                "right": "Ignore the monkey and press on",
                "left_node": "1RRL",
                "right_node": "1RRR",
            },
            "1RRL": {
                "text": (
                    "The monkey leads you through the treetops. Theres lots of monkeys jumping from branch to branch. It's like a highway up here. "
                    "The monkey stops and drops your hat. In dismay you look down but to your delight you can see its falling towards the elephant herd. The baby elephant has already started to run towards your hat."
                    "You turn around to thank the monkey but he has vanished. You scramble down the tree and catch up with the baby elephant who was surprised to see the other elephants. Since he was just trying to get your hat for you. He excitedly runs towards his mother who pulls him into an embrace. Theres many happy trumpets and the elephants look very grateful. You dust off your hat and happily go on your way."
                
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1RRR": {
                "text": (
                    "You press on through increasingly thick foliage. You pause to take a breathe and the baby elephant pushes ahead of you to use his trunk to push branches aside for you "
                    "Eventually you both stumble out of the trees onto a wide plain"
                    "to find the herd just fifty metres away. Sometimes the direct route works. The baby elephant runs towards his mother who was so worreid about him. They are both so happy to be reunited. The mother gives you a grateful look. You are so happy you could help out the baby elephant before you even had your lunch."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
        },
    },

    # STORY 2: The Stolen River Stone
    {
        "title": "The Stolen River Stone",
        "intro": (
            "It's a hot day and you are paddling a canoe down a slow river when something catches your eye. "
            ". In the riverbed you can see a glowing green stone. It looks bautiful. As you get closer and begin to reach for it an otter swims up and snatches it. "
            "They quickly swim away. "
        ),
        "nodes": {
            "1": {
                "text": (
                    "The otter pops up downstream, it's gripping the glowing stone in it's mouth and watching you with bright eyes. "
                    "Press the left button to Dive in and swim after it. Press the right button to paddle the canoe hard to cut it off "
                ),
                "left": "Dive in and swim after it",
                "right": "Paddle the canoe to cut it off",
                "left_node": "1L",
                "right_node": "1R",
            },

            "1L": {
                "text": (
                    "You dock your canoe and jump into the water. The water is cool and clear. You begin to swim towards the otter. The other watches with some interest. As you get closer it begins to swim away"
                    "The otter is fast and keeps glancing back as if this is a game. It ducks under a waterlogged tree. "
                    "Press the left button to Squeeze under the log. Press the right button to Swim around the log."
                ),
                "left": "Squeeze under the log",
                "right": "Swim around the log",
                "left_node": "1LL",
                "right_node": "1LR",
            },
            "1LL": {
                "text": (
                    "As you swim under the log it seems you have disturbed a habitat of hundered of tiny fish. They scatter as you swim past.  "
                    "You emerge from the water too see the otter waiting patiently for you on a muddy bank. The otter drops the stone and takes some time to sniff you curiously. "
                    "But now you notice the stone is cracked. "
                    "Press the left button to take the cracked stone. Press the right button to leave it for the river."
                ),
                "left": "Take the cracked stone",
                "right": "Leave it for the river",
                "left_node": "1LLL",
                "right_node": "1LLR",
            },
            "1LLL": {
                "text": (
                    "You carry the stone home and that night leave it on your windowsill. Overnight it glows a soft green and the crack slowly heals itself. "
                    "By morning it's back in one piece. "
                    "Press the left button to keep the stone. Press the right button to return the stone to the river."
                ),
                "left": "Keep it",
                "right": "Return it to the river",
                "left_node": "1LLLL",
                "right_node": "1LLLR",
            },
            "1LLLL": {
                "text": (
                    "You sit the stone on your shelf and it sits there for many years glowing softly."
                    "Every time you feel sad or lonely in life it seems to glow a little brighter."
                    "You never find out what it truly is but maybe some mysteries are best left unsolved."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1LLLR": {
                "text": (
                    "You wade through the river, your eyes set on where you saw the stone initially. Once you reach the spot you bend down and drop the stone back into the water. "
                    "You jump as the whole river begins shimmering green just for a second before returning to its natural colour. "
                    "The otter walks closer to you and bows its head."
                    "You get the feeling you did something important even if you don't know what."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLR": {
                "text": (
                    "You leave the stone on the muddy river bank. All of a sudden a heron swoops in and grabs the stone. It begins to fly upriver. "
                    "The otter begins to follow the heron. The situation is so odd that you decide to follow the otter. You go back into your canoe and begin rowing it. The otter spots you in the canoe and hops in for the ride. You both follow the heron. "
                    "The heron leads both of you to a small island "
                    "It is covered in the most beautiful flowers and fruit you have ever seen. Is this your reward?"
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1LR": {
                "text": (
                    "As you are swimming around the log you spot an underwater cave entrance. You can see the glowing stone sitting in the cave."
                    "Press the left button to swim into the cave. Press the right button to surface and look for another way in."
                ),
                "left": "Swim into the cave",
                "right": "Surface and find another way",
                "left_node": "1LRL",
                "right_node": "1LRR",
            },
            "1LRL": {
                "text": (
                    "You dive into the cave. Its small and dark but you keep swimming and following the glow of the stone. The cave opens into an air pocket and you can see the stone within your reach."
                    "The otter is there too, watching you. It picks up the stone and places it gently in your hands."
                    "It seems like the otter was guarding the stone for you all along."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1LRR": {
                "text": (
                    "A little further along the river you find a large clump of roots all twisted together. You use it as a rope to climb down and get into the cave from another entrance. You retrieve the stone from a shallow ledge just inside your newly discovered entrance. "
                    "As you leave the cave and sit on the river bank to dry off a rainbow appears over the river. But it hasn't been raining today. "
                    "Some things in the jungle defy explanation."
                ),
                "ending": True,
                "ending_type": "surprise",
            },

            "1R": {
                "text": (
                    "You paddle furiously to get ahead of the otter. "
                    "As you speed up the canoe cuts the otter off. It surfaces right beside your canoe, stone in mouth and looking very impressed. "
                    "It drops the stone into your canoe and swims away. As you feel the sotne in your hand you notice it's quite warm and almost vibrating. "
                     "You notice it is pointing like a compass. "
                    "Press the left button to follow where the stone points. Press the right button to paddle back to your home."
                ),
                "left": "Follow where the stone points",
                "right": "Paddle back to camp",
                "left_node": "1RL",
                "right_node": "1RR",
            },
            "1RL": {
                "text": (
                    "You set the stone in your lap as you begin to paddle while following the stone's direction. The stone leads you to a part of the rive you have never seen before. "
                    "You can see an old stone archway up ahead. "
                    "Press the left button to paddle through the archway. Press the right button to paddle around it."
                ),
                "left": "Paddle through the archway",
                "right": "Circle around it",
                "left_node": "1RLL",
                "right_node": "1RLR",
            },
            "1RLL": {
                "text": (
                    "You paddle through the archway. Before your own eyes the jungle transforms."
                    "The trees are taller, the flowers more vivid, the water sparkling. "
                    "Animals slowly gather at the river bank as they watch you. The stone stops vibrating and glowing. This seems to be where it wants you to be."
                    "Press the left button to step ashore. Press the right button to turn back."
                ),
                "left": "Step ashore",
                "right": "Turn back",
                "left_node": "1RLLL",
                "right_node": "1RLLR",
            },
            "1RLLL": {
                "text": (
                    "You spend an afternoon in the most beautiful place imaginable. You eat tasty fruit, the river water tastes better here too. The animals are very friendly, none of them are shy. When it gets dark you reluctantly leave. "
                    "As you paddle home you notice the stone going dark and cold."
                    "It's magic may be used up but the memory of that day will stay with you forever."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLLR": {
                "text": (
                    "Something doesn't feel quite right so you decide to turn your canoe arounf and paddle back through the archway. "
                    "When you glance behind you, the archway is gone"
                    "You look down at the stone on your lap as it turns to an ordinary pebble. But you know what you saw."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1RLR": {
                "text": (
                    "As you paddle around the archway you feel the stone going cold. "
                    "It distracts you for a moment until a fish leaps out of the river and into your boat. The fish flounders desperately onboard. It thrashes wildly and almost tips over your small canoe. You quickly pick up the fish and throw it back in the river. You watch it swim away. "
                    "As you look around your boat you realise the fish must have snatched the stone. The otter surfaces, looking disappointed before swimming away. "
                    "You learn that some stories don't have a good ending."
                ),
                "ending": True,
                "ending_type": "mishap",
            },
            "1RR": {
                "text": (
                    "You return home and set the stone on a shelf. You're exhausted so after cooking dinner you go right to bed. That night you dream of the otter coming to your house and showing you an underground river full of glowing stones."
                    "In the morning you awake to find that the stone is gone. But so are your muddy boots, someone cleaned them!."
                    "Press the left button to go back to find the otter. Press the right button to accept the mystery."
                ),
                "left": "Go back to find the otter",
                "right": "Accept the mystery",
                "left_node": "1RRL",
                "right_node": "1RRR",
            },
            "1RRL": {
                "text": (
                    "You spend three full days searching but never find the otter again. "
                    "On the last day as you desperatly wade through the river, tired and frustrated a green light pulses once from deep within the river, "
                    "and you feel certain it is a goodbye. It gives you the closure to end your search"
                    "Some friends are only meant to cross your path once."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1RRR": {
                "text": (
                    "You accept it the mystery for what it is. Clean boots, strange dreams, and a beautiful stone. You know you won't be able to figure it out. "
                    "That evening a letter arrives at your door. You don't notice it until the next morning as you open your door. "
                    "You open the letter. It is a page covered in very cute paw prints. "
                    "You still have no idea what any of this meant."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
        },
    },

    # STORY 3: The Night the Jungle Went Dark
    {
        "title": "The Night the Jungle Went Dark",
        "intro": (
            "You are on your way home from your nightly walk. You love living in the jungle. Even if sometimes it's a bit lonely."
            "You jump as every single light goes out at once. There's not many light sources in the jungle but the fireflies stop glowing and your lantern stops working. "
            "You stand still, taking in what happened in complete darkness. "
            "Then, from somewhere near you hear a very small voice whisper"
            "Hello? Is someone there? I need help."
        ),
        "nodes": {
            "1": {
                "text": (
                     "The voice is coming from something small on the ground. You don't want to hurt it by accident so you stand still while fumbling around for your matches."
                    "You find them and make a tiny flame. It's the only light you'l have for now. With this light you see a you see a young loris sitting in your path, "
                    "Its enormous eyes are reflecting back at you. "
                    "The light-keeper has gone missing and without her the jungle stays dark, it says very seriously. "
                    "Press the left button to follow the loris now."
                    "Press the right button to go back to your home for supplies first."
                ),
                "left": "Follow the loris immediately",
                "right": "Go back to camp for supplies",
                "left_node": "1L",
                "right_node": "1R",
            },

            "1L": {
                "text": (
                    "As you follow the loris you are surpsied with how fast she moves. She brings you to an enormous grove of faintly glowing mushrooms. The mushrooms are the size of trees. It's just enough light to see by so you blow out your match. You can see in the middle of the mushrooms there's a hole in the ground. You can hear something crying."
                    "Press the left button to climb down into the hole. Press the right button to call down into it first."
                ),
                "left": "Climb down",
                "right": "Call into it first",
                "left_node": "1LL",
                "right_node": "1LR",
            },
            "1LL": {
                "text": (
                    "You climb down into an underground home. "
                    "You can see the light-keeper in the corner. It turns out the light-keeper is a tiny firefly queen."
                    "But she's trapped as her wings are tangled in a spider's web. "
                    "She looks relieved as she reliases she will be helped. "
                    "Press the left button to untangle her wings yourself. "
                    "Press the right button to ask the loris to help with its nimble fingers."
                ),
                "left": "Untangle her yourself",
                "right": "Ask the loris to help",
                "left_node": "1LLL",
                "right_node": "1LLR",
            },
            "1LLL": {
                "text": (
                    "You are worried as you don't know when the spider will be back or how big it will be so you decide to try it yourself."
                    "Your fingers are clumsy so you work patiently and slowly to untangle each thread of the web."
                    "When the last thread comes free the firefly queen rises into the air and lights up like a tiny sun. You stand in awe as you watch her. "
                    "Outside, millions of fireflies answer her call and the jungle returns to a comfortable glow. You did it by yourself."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLR": {
                "text": (
                   "You watch on impressed as the loris works with extraordinary delicacy, humming to itself as it unpicks each thread perfectly. "
                    "When the last thread comes free the firefly queen rises into the air and lights up like a tiny sun. You stand in awe as you watch her. "
                    "Outside, millions of fireflies answer her call and the jungle returns to a comfortable glow."
                    "You couldn't have done it without a friend."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LR": {
                "text": (
                    "As you call down a tiny voice answers: My wings are stuck! I can't get out!. "
                    "The loris tugs your sleeve and explains that she will need something to grab onto. "
                    "Press the left button to lower your scarf into the hole. Press the right button to find a long stick."
                ),
                "left": "Lower your scarf",
                "right": "Find a long stick",
                "left_node": "1LRL",
                "right_node": "1LRR",
            },
            "1LRL": {
                "text": (
                    "The firefly queen grabs your scarf and you hauled her up gently."
                    "In the open air she shakes herself free of the scarf."
                    "The firefly queen rises into the air and lights up like a tiny sun. You stand in awe as you watch her. "
                    "Outside, millions of fireflies answer her call and the jungle returns to a comfortable glow."
                    "The loris giddily claps her tiny hands. Your scarf now fainlty glows forever."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1LRR": {
                "text": (
                    "You grab the first stick you find. It's a little thin but it will have to do. But as the queen grabs onto the stick and you begin to pull her up the stick snaps!"
                    "She falls down with a small squeak. You scramble down to check on her. She's alright but is stuck on a spiderweb. "
                    "You are worried as you don't know when the spider will be back or how big it is."
                    "Your carefully untangle each thread of the web from her wings."
                    "Once she's freed the firefly queen rises into the air and lights up like a tiny sun. You stand in awe as you watch her. "
                    "Outside, millions of fireflies answer her call and the jungle returns to a comfortable glow. It took a bit longer than you thought but you were able to free her in the end."
                ),
                "ending": True,
                "ending_type": "mishap",
            },

            "1R": {
                "text": (
                    "Back at your house you fill a backpack with a torch, rope and some food just in case. "
                    "When you go back outside you see the loris is impatiently tapping its foot. Now that your both ready the loris begins to lead you to a vast dark lake that you have never seen before. "
                    "A ricket boat is tied at the edge of the lake. "
                    "Press the left button to take the boat across the lake. Press the right button to walk around the shore."
                ),
                "left": "Take the boat across",
                "right": "Walk around the shore",
                "left_node": "1RL",
                "right_node": "1RR",
            },
            "1RL": {
                "text": (
                    "The lake is eerily still and black as ink. You pull your torch out of your bag and turn it on, surprisingly it works. You hold the torch in your mouth as you get into the boat, unhook it and begin to row. In the distance the torchlight shows the outline of a tiny island."
                    "You can see on the island that there is a glass jar with something glowing inside. "
                    "Press the left button to row straight for the jar. Press the right button to circle the island first."
                ),
                "left": "Row straight for the jar",
                "right": "Circle the island first",
                "left_node": "1RLL",
                "right_node": "1RLR",
            },
            "1RLL": {
                "text": (
                    "You row straight to the islands shore and open the jar to find the firefly queen peacefully asleep inside. It seems someone trappped her in this jar."
                    "As you open the lid and she wakes with a start and shoots into the sky glowing brightly. You watch as the whole lake lighs up. "
                    "Millions of fireflies answer her call and the jungle returns to a comfortable glow. You row back through the most beautiful light show you've ever seen."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLR": {
                "text": (
                    "As you circle around the island your eyes adjust better to the low light and you can see it's not an island but a mass of leaves. Lucky for you that you didn't try to step onto it. Still in the boat you reach over and grab the jar. "
                    "As you look in the jar you can see the firefly queen peacefully asleep inside. It seems someone trappped her in this jar."
                    "As you open the lid and she wakes with a start and shoots into the sky glowing brightly. You watch as the whole lake lighs up. "
                    "Millions of fireflies answer her call and the jungle returns to a comfortable glow. You row back through the most beautiful light show you've ever seen but you're glad that your caution paid off.."
                ),
                "ending": True,
                "ending_type": "triumph",
            },
            "1RR": {
                "text": (
                    "That boat doesn't look safe so you decide to walk. The shore path is longer but there's a trail of glowing paw prints leading into the trees. "
                    "The loris sees them too and whispers: The thief must have went this way. "
                    "Press the left button to follow the paw prints. Press the right button to stick to the shoreline."
                ),
                "left": "Follow the paw prints",
                "right": "Stick to the shore",
                "left_node": "1RRL",
                "right_node": "1RRR",
            },
            "1RRL": {
                "text": (
                    "The paw prints lead to a pangolin that is fast asleep. "
                    "You can see that the firefly queen is trapped in its scales. She must have rolled in by accident! She is relieved to see you. "
                    "You gently approach the pangolin and uncurl it. "
                    "The queen tumbles free from the pangolin's scales. She stretches her wings and rises into the night sky, her glow almost dazzling. "
                    "Millions of fireflies answer her call and the jungle returns to a comfortable glow.
                    "The pangolin snores through the whole thing completely oblivious to what happenend."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
            "1RRR": {
                "text": (
                    "You stick to the shore and eventually find a small beach."
                    "The loris runs ahead to a rock pool and you follow her. Inside you peer in and you can see the firefly queen is sitting in the rock pool. She looks very unhappy and her wings are soaking wet. "
                    "She just fell in. You carefully scoop her out of the water and pat down her wings with your scarf. Once she's dry she seems much happier."
                    "She lights up and zips around you flutteirng her wings before rising into the sky. Millions of fireflies answer her call and the jungle returns to a comfortable glow."
                ),
                "ending": True,
                "ending_type": "surprise",
            },
        },
    },
]
