from flask import Flask
from sqlalchemy import QueuePool
import os
from config.extensions import cache


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool": QueuePool,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }

    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 5
    CACHE_REDIS_URL = os.getenv("REDIS_URL")
    CACHE_KEY_PREFIX = os.getenv("APP_NAME")


def create_app() -> Flask:
    """Application factory pattern."""

    app = Flask(__name__)
    app.config.from_object(Config)
    cache.init_app(app)
    return app
