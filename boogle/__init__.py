"""Define method to create app instances."""
from flask import Flask
from flask_bootstrap import Bootstrap

from boogle.main import main as main_blueprint
from boogle.books import books as books_blueprint
from boogle.config import app_config


def create_app(app_env):
    app = Flask(__name__)
    app.config.from_object(app_config[app_env])
    
    # Use bootstrap dependency for views
    Bootstrap(app)

    # Register app blueprints.
    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(books_blueprint, url_prefix='/books')
    return app
