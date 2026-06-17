from decimal import Decimal

from sqlalchemy import String, Text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from order_service.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=True)
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="product")
