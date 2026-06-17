from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from order_service.db import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    orders: Mapped[list["Order"]] = relationship(back_populates="client")