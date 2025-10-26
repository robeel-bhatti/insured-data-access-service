from src.models.address import Address
from src.models.party import Party
from src.repository.abstract_repository import AbstractRepository


class PartyService:
    def __init__(
        self,
        party_repository: AbstractRepository[Party],
        address_repository: AbstractRepository[Address],
    ):
        self.party_repository = party_repository
        self.address_repository = address_repository
