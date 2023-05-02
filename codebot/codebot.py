import os
import openai

from dotenv import load_dotenv, find_dotenv
from typing import List

from .utils import get_completion_from_messages, chop_text


class CodeBot:

    _api_key: str
    _context: List = []
    _chop_text: bool

    def __init__(self, initial_context: str = None, chop_text: bool = True):
        _ = load_dotenv(find_dotenv())

        self._api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self._api_key

        self._context = [{
            "role": "system",
            "content": initial_context or "You are a chatbot. Salute the user."
        }]

        self._chop_text = chop_text

    def run(self):
        msg_wrap = "CodeBot: {}\nYou: "
        try:
            while True:
                # Generating response
                res = get_completion_from_messages(messages=self._context)
                self._context.append({
                    "role": "assistant",
                    "content": res,
                })

                # Getting user's input
                if self._chop_text:
                    inp = input(chop_text(msg_wrap.format(res)))
                else:
                    inp = input(msg_wrap.format(res))

                self._context.append({
                    "role": "user",
                    "content": inp,
                })
        except KeyboardInterrupt:
            print("\nBye!")
