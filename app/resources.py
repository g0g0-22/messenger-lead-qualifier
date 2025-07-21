from flask_restx import Resource, Namespace

ns = Namespace("api")


@ns.route("/webhook")
class Webhook(Resource):
    def get(self):
        return {"hello": "madafakas"}
