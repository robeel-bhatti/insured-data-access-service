from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import QueuePool
from redis import Redis
import os


class Config:
    DEBUG = True


def create_app() -> Flask:
    """Application factory pattern."""

    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    init_cache(app)
    return app


def init_db(app: Flask) -> None:
    options = {
        "poolclass": QueuePool,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }

    url = os.getenv("DATABASE_URL")
    if url is None:
        raise Exception(
            "App failed to start because the environment variable 'DATABASE_URL' is not set"
        )

    engine = create_engine(url, **options)
    session = sessionmaker(bind=engine)
    app.session = session()


def init_cache(app: Flask) -> None:
    url = os.getenv("CACHE_URL")
    if url is None:
        raise Exception(
            "App failed to start because the environment variable 'REDIS_URL' is not set"
        )

    cache = Redis.from_url(url)
    app.cache = cache
