from dotenv import load_dotenv
import os
from openai import OpenAI

# load_dotenv()

_client = None  # lazy singleton so imports are cheap


def get_client() -> OpenAI:
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        _client = OpenAI(api_key=api_key)
    return _client


def generate_reply(prompt: str, model: str = "gpt-4o") -> str:
    client = get_client()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content
