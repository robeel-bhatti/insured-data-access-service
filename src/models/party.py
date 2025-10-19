from typing import Optional, List
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.address import Address
from models.party_history import PartyHistory


class Party(Base):
    """Party table model"""

    __tablename__ = "party"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    middle_name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(10))
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
    hash: Mapped[str] = mapped_column(Text)
    address: Mapped["Address"] = relationship(back_populates="parties")
    history_records: Mapped[List["PartyHistory"]] = relationship(back_populates="party")
