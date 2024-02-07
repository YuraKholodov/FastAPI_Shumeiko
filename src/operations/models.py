from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Operation(Base):
    __tablename__ = "operation"

    quantity: Mapped[str]
    figi: Mapped[str]
    instrument_type: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime] = mapped_column(TIMESTAMP)
    type: Mapped[str]
