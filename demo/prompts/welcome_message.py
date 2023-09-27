from typing import List


def build_welcome_message(messages: List[str]) -> str:
    # TODO: Return a randomaised welcome_message
    return messages[1]


messages = ["Hello there! I'm ComSum AI, your AI personal assistant",
"Hey, how can I help you today?",
"...."
]

welcome_message = {"role": "assistant", "content": f"{build_welcome_message(messages)}"}
