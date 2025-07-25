import os
from flask import request
from flask_restx import Resource, Namespace
from flask import make_response
from .facebook.sendMessage import sendMessage
from .ai.responseAi import respond_ai
from .db.data import add_message, get_conversation
from .facebook.getUsername import get_username
ns = Namespace("api")

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PAGE_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
if VERIFY_TOKEN is None:
    raise EnvironmentError(
        "VERIFY_TOKEN is not set. Did you forget the .env file?")
if PAGE_TOKEN is None:
    raise EnvironmentError(
        "PAGE_TOKEN is not set. Did you forget the .env file?")


@ns.route("/webhook")
class Webhook(Resource):
    def get(self):
        print("✅ /webhook GET hit")
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        print("🔹 mode:", mode)
        print("🔹 token from Facebook:", repr(token))
        print("🔹 expected VERIFY_TOKEN:", repr(VERIFY_TOKEN))
        print("🔹 challenge:", challenge)

        if mode == "subscribe" and token == VERIFY_TOKEN:
            response = make_response(challenge, 200)
            response.mimetype = "text/plain"
            return response
        else:
            return {"error": "Forbidden"}, 403

    def post(self):
        data = request.get_json()
        print("Event received:", data)
        recipientId = data["entry"][0]["messaging"][0]["sender"]["id"]
        text = data["entry"][0]["messaging"][0]["message"]["text"]
        add_message(recipientId, get_username(uid=recipientId), "user", text)

        conversation = get_conversation(recipientId)
        respond_ai(recipientId, conversation)

        # print("✅CONVERSATION:", get_conversation(recipientId))
        # sendMessage(recipient_id=recipientId, message_text=text)
        return {"status": "EVENT_RECEIVED"}, 200
