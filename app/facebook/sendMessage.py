import os
import requests
from ..db.data import add_message
# from dotenv import load_dotenv

# load_dotenv()
PAGE_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


def sendMessage(recipient_id: str, message_text: str):
    url = "https://graph.facebook.com/v18.0/me/messages"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
        "messaging-type": "RESPONSE"
    }
    params = {
        "access_token": PAGE_TOKEN
    }
    response = requests.post(url, params=params, json=payload, headers=headers)
    add_message(recipient_id, " ", "assistant", message_text)
    print("Status:", response.status_code)
    print("Response:", response.text)
