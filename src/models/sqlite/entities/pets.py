from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String

from src.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"PetsTable(id={self.id}, name={self.name}, type={self.type})"
