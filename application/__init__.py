from flask import Flask
from flask_cors import CORS
from ..config import Config
from .collector.routes import collector_routes
from .services import create_coin_market_cap_service


def create_app():
    """Factory to create the Flask application
    :return: A `Flask` application instance
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        app.coin_market_cap_service = create_coin_market_cap_service()

    # Initialize extensions
    # Register blueprints
    # Other setup tasks

    _register_blueprints(app)
    CORS(app)
    return app


def _register_blueprints(app):
    app.register_blueprint(collector_routes)
