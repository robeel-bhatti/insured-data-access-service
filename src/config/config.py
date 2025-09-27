from flask import Flask
from sqlalchemy import QueuePool


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool": QueuePool,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }


def create_app() -> Flask:
    """Application factory pattern."""

    app = Flask(__name__)
    app.config.from_object(Config)
    return app
