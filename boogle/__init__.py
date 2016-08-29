"""Define method to create app instances."""

from flask import Flask

from boogle.config import app_config


def create_app(app_env):
    app = Flask(__name__)
    app.config.from_object(app_config[app_env])
    return app
