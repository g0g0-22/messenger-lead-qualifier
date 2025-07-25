from dotenv import load_dotenv
import os
from openai import OpenAI
from ..db.data import get_conversation
from ..facebook.sendMessage import sendMessage
from ..facebook.getUsername import get_username
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


def normalize_conversation(conversation):
    normalized = []
    for sender, text in conversation:
        role = "user" if sender == "user" else "assistant"
        normalized.append({"role": role, "content": text})
    return normalized


def respond_ai(uid, conversation):
    conversation = normalize_conversation(conversation=conversation)
    username = get_username(uid=uid)
    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"""
                    You are a helpful travel assistant for a travel agency.
                    Your goal is to qualify leads by gathering all necessary booking information:
                    destination, dates, number of guests, accommodation preferences, and any other relevant travel details.
                    At the start, address the user by their first name: {username.split(" ")[0]}

                    After every message from the user, check the full conversation.
                    If you now have **enough information** to make a full summary of their request, start your message with [SUMMARY] and then reply with:
                    1. A clear and concise summary of what they want.
                    2. A final "Thank you, an agent will follow up with you soon!" message.

                    If you still need more information, continue the conversation naturally and ask the next most relevant question.
                    """
            },
            *conversation
        ]
    )
    content = response.choices[0].message.content
    if content.startswith("[SUMMARY]"):
        summary_text = content.split("[SUMMARY]")[1].strip()
        # add_summary_to_sheets(uid, summary_text)
        sendMessage(
            uid, f"Thank you for your interest, {username.split(" ")[0]}. An agent will contact you soon!")
    else:
        sendMessage(uid, content)
