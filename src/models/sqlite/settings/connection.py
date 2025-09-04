from sqlalchemy import create_engine


class DBConnectionHandler:
    def __init__(self):
        self.__db_path = "sqlite:///storage.db"
        self.__engine = None

    def connect(self):
        self.__engine = create_engine(self.__db_path, echo=True)

    def get_engine(self):
        return self.__engine
