from sqlalchemy import Engine
from .connection import DBConnectionHandler


# @pytest.mark.skip(reason="")
def test_db_connection_handler():

    db_handler = DBConnectionHandler()
    assert db_handler.get_engine() is None

    db_handler.connect()
    engine = db_handler.get_engine()
    assert engine is not None
    assert str(engine.url) == "sqlite:///storage.db"
    assert isinstance(engine, Engine)
