import os
from flask import Flask


class Config:

    DEBUG = True

    # Database Configuration - In-Memory SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'echo': False  # Set to True for SQL query logging
    }

    # JSON Configuration
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    JSONIFY_PRETTYPRINT_REGULAR = True

    # Logging
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


def create_app():
    """Application factory pattern."""

    app = Flask(__name__)
    app.config.from_object(Config)
    return app
