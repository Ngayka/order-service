from decimal import Decimal

from sqlalchemy import Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import mapped_column, Mapped, relationship

from order_service.db.base import Base


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id"), nullable=False)
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="order")
    client: Mapped["Client"] = relationship(back_populates="orders")


class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    price_at_order: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    quantity: Mapped[int] = mapped_column(default=1, nullable=False)
    order: Mapped["Order"] = relationship(back_populates="order_items")
    product: Mapped["Product"] = relationship(back_populates="order_items")