from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import Column
from sqlalchemy import BIGINT


class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = "Address"

    id: Mapped[int] = Column(BIGINT, primary_key=True)
