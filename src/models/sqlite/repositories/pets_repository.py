from typing import List
from sqlalchemy.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable


class PetsRepository:

    def __init__(self, db_connection) -> None:
        self.__db_conection = db_connection

    def list_pests(self) -> List:
        with self.__db_conection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets

            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_conection as database:
            try:
                (database.session
                 .query(PetsTable)
                 .filter(PetsTable.name == name)
                 .delete()
                 )
                database.session.commit()
            except Exception as exception:
                database.session.rollbak()
                raise exception
