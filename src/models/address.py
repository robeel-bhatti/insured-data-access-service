from typing import Optional, List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from models.party import Party


class Address(Base):
    """Address table model"""

    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    street_one: Mapped[str] = mapped_column(String(50))
    street_two: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(2))
    zip_code: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(3))
    hash: Mapped[str] = mapped_column(Text)
    parties: Mapped[List["Party"]] = relationship(back_populates="address")
