import openai

from time import sleep
from typing import Iterable


def get_completion_from_messages(messages: Iterable[dict], model="gpt-3.5-turbo", temperature=0):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
    except openai.error.RateLimitError:
        sleep(20)
        return get_completion_from_messages(messages, model, temperature)
    return response.choices[0].message["content"]


def chop_text(text: str, length: int = 120) -> str:
    return "\\\n".join(
        [
            text[i:i+length]
            for i in range(0, len(text), length)
        ]
    )