from typing import Optional

from sqlalchemy.orm import Session

from repository.abstract_repository import AbstractRepository
from src.models.address import Address
from src.models.party import Party
from src.repository.address_repository import AddressRepository
from src.repository.party_repository import PartyRepository
from src.service.party_service import PartyService


class Container:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
        self._party_repository: Optional[AbstractRepository[Party]] = None
        self._address_repository: Optional[AbstractRepository[Address]] = None
        self._party_service: Optional[PartyService] = None

    @property
    def party_repository(self) -> AbstractRepository[Party]:
        if not self._party_repository:
            self._party_repository = PartyRepository(self.db_session)
        return self._party_repository

    @property
    def address_repository(self) -> AbstractRepository[Address]:
        if not self._address_repository:
            self._address_repository = AddressRepository(self.db_session)
        return self._address_repository

    @property
    def party_service(self) -> PartyService:
        if not self._party_service:
            self._party_service = PartyService(
                self.party_repository, self.address_repository
            )
        return self._party_service
