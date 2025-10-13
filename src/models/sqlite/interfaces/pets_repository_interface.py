from typing import List
from abc import ABC, abstractmethod

class PetsRepositoryInterface(ABC):

    @abstractmethod
    def list_pests(self) -> List:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
