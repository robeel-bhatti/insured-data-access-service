from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import QueuePool
import os


class Config:
    DEBUG = True


def create_app() -> Flask:
    """Application factory pattern."""

    app = Flask(__name__)
    app.config.from_object(Config)
    return app


def init_db(app: Flask) -> None:
    options = {
        "poolclass": QueuePool,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }

    url = os.getenv("DATABASE_URL")
    if url is None:
        raise Exception("DATABASE_URL is not set")

    engine = create_engine(url, **options)
    session = sessionmaker(bind=engine)
    app.session = session()
