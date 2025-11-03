import pytest
from src.models.sqlite.settings.connection import DBConnectionHandler
from .pets_repository import PetsRepository
from .people_repository import PeopleReposity

db_connection_handler = DBConnectionHandler()

db_connection_handler.connect()


@pytest.mark.skip(reason="teste de integracao")
def test_list_pets():
    repository = PetsRepository(db_connection_handler)

    pets = repository.list_pets()
    print()
    print(pets)


@pytest.mark.skip(reason="teste de integracao")
def test_delete_pet():
    name = "paco"
    repository = PetsRepository(db_connection_handler)
    repository.delete_pets(name)
    pets = repository.list_pets()
    print()
    print(pets)


@pytest.mark.skip(reason="teste de integracao")
def test_insert_person():
    first_name = "John"
    last_name = "Doe"
    age = 50
    pet_id = 2

    repository = PeopleReposity(db_connection_handler)
    repository.insert_person(first_name, last_name, age, pet_id)


def test_get_person():
    person_id = 1

    repository = PeopleReposity(db_connection_handler)
    person = repository.get_person(person_id)

    (first_name, last_name, pet_name, pet_type,) = person
    print(first_name)
    print(last_name)
    print(pet_name)
    print(pet_type)
