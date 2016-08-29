"""Define method to create app instances."""

from flask import Flask


def create_app(work_env):
    app = Flask(__name__)
    return app
