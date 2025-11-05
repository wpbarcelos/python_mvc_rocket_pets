from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, BIGINT, String, ForeignKey
from src.models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = 'people'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    pet_id: Mapped[int | None] = mapped_column(ForeignKey("pets.id"), nullable=True)


    def __repr__(self) -> str:
        return (f"<People(id={self.id}, first_name='{self.first_name}', "
                f"last_name='{self.last_name}', age={self.age}, pet_id={self.pet_id})>")
