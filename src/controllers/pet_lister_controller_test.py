from .pet_lister_controller import PetListerController


class MockPestTable:
    def __init__(self, name: str, pet_type: str, pet_id: int):
        self.id = pet_id
        self.type = pet_type
        self.name = name


class MockPetsRepository:
    def list_pets(self) -> list[MockPestTable]:
        return [
            MockPestTable(name="Fluffy", pet_type="cat", pet_id=4),
            MockPestTable(name="Buddy", pet_type="dog", pet_id=42),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "type": "cat", "id": 4},
                {"name": "Buddy", "type": "dog", "id": 42}
            ]
        }
    }

    assert response == expected_response
