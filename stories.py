STORIES = [
    {
        "title": "Test Story",
        "intro": "Test start.",
        "nodes": {
            "1": {
                "text": "Node one.",
                "left": "go left",
                "right": "go right",
                "left_node": "1L",
                "right_node": "1R",
            },

            "1L": {
                "text": "You went left.",
                "left": "go left",
                "right": "go right",
                "left_node": "1LL",
                "right_node": "1LR",
            },
            "1LL": {
                "text": "Left left.",
                "left": "go left",
                "right": "go right",
                "left_node": "1LLL",
                "right_node": "1LLR",
            },
            "1LLL": {
                "text": "Left left left.",
                "left": "go left",
                "right": "go right",
                "left_node": "1LLLL",
                "right_node": "1LLLR",
            },
            "1LLLL": {
                "text": "Ending. Left left left left.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLLR": {
                "text": "Ending. Left left left right.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLR": {
                "text": "Left right.",
                "left": "go left",
                "right": "go right",
                "left_node": "1LLRL",
                "right_node": "1LLRR",
            },
            "1LLRL": {
                "text": "Ending. Left left right left.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1LLRR": {
                "text": "Ending. Left left right right.",
                "ending": True,
                "ending_type": "mishap",
            },
            "1LR": {
                "text": "Left right.",
                "left": "go left",
                "right": "go right",
                "left_node": "1LRL",
                "right_node": "1LRR",
            },
            "1LRL": {
                "text": "Ending. Left right left.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1LRR": {
                "text": "Ending. Left right right.",
                "ending": True,
                "ending_type": "mishap",
            },

            "1R": {
                "text": "You went right.",
                "left": "go left",
                "right": "go right",
                "left_node": "1RL",
                "right_node": "1RR",
            },
            "1RL": {
                "text": "Right left.",
                "left": "go left",
                "right": "go right",
                "left_node": "1RLL",
                "right_node": "1RLR",
            },
            "1RLL": {
                "text": "Right left left.",
                "left": "go left",
                "right": "go right",
                "left_node": "1RLLL",
                "right_node": "1RLLR",
            },
            "1RLLL": {
                "text": "Ending. Right left left left.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLLR": {
                "text": "Ending. Right left left right.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLR": {
                "text": "Right left right.",
                "left": "go left",
                "right": "go right",
                "left_node": "1RLRL",
                "right_node": "1RLRR",
            },
            "1RLRL": {
                "text": "Ending. Right left right left.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1RLRR": {
                "text": "Ending. Right left right right.",
                "ending": True,
                "ending_type": "triumph",
            },
            "1RR": {
                "text": "Right right.",
                "left": "go left",
                "right": "go right",
                "left_node": "1RRL",
                "right_node": "1RRR",
            },
            "1RRL": {
                "text": "Ending. Right right left.",
                "ending": True,
                "ending_type": "surprise",
            },
            "1RRR": {
                "text": "Ending. Right right right.",
                "ending": True,
                "ending_type": "triumph",
            },
        },
    },
]
