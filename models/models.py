from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import JSON, TIMESTAMP, ForeignKey


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Role(Base):
    __tablename__ = 'roles'

    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[str] = mapped_column(JSON)


class User(Base):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), nullable=True)
