from flask import Flask
from dotenv import load_dotenv
import os
from .db.data import init_db
from flask import make_response
from .resources import ns
from flask_restx import Api
load_dotenv()  # Load variables from .env into os.environ


def create_app():
    api = Api()
    app = Flask(__name__)
    init_db()
    api.init_app(app)
    api.add_namespace(ns, path="/api")
    return app
