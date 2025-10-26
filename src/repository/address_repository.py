from sqlalchemy.orm import Session

from src.models.address import Address
from src.repository.abstract_repository import AbstractRepository


class AddressRepository(AbstractRepository[Address]):
    def __init__(self, session: Session):
        self.session = session

    # def get_all(self, query: str) -> list[Address]:
    #     pass

    def get_by_id(self, id: int) -> Address:
        return self.session.get_one(entity=Address, ident=id)

    def add(self, entity: Address) -> None:
        self.session.add(entity)

    def delete(self, id: int) -> None:
        self.session.delete(instance=Address)
