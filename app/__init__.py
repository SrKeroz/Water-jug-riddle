#Flask
from flask import Flask

#Directory
from .api import api

#Config
from app.config import Config

# creating app
def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(api)

    return app