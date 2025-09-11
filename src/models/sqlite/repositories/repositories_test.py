import pytest
from src.models.sqlite.settings.connection import DBConnectionHandler
from .pets_repository import PetsRepository
db_connection_handler = DBConnectionHandler()

db_connection_handler.connect()


@pytest.mark.skip(reason="teste de integracao")
def test_list_pets():
    repository = PetsRepository(db_connection_handler)

    pets = repository.list_pests()
    print()
    print(pets)


def test_delete_pet():
    name = "paco"
    repository = PetsRepository(db_connection_handler)
    repository.delete_pets(name)
    pets = repository.list_pests()
    print()
    print(pets)
