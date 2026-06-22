from decimal import Decimal

from sqlalchemy.orm import Session

from order_service.models import OrderItem, Order, Client
from order_service.schemas.order import OrderCreateSchema, OrderReadSchema
from order_service.service.product_service import ProductService


class OrderService:
    @staticmethod
    def create(order_data: OrderCreateSchema, db: Session):
        if not order_data.order_items:
            raise ValueError("Order must contain minimum one product")
        client = db.query(Client).filter(Client.id == order_data.client_id).first()
        if not client:
            raise ValueError(f"Client {order_data.client_id} not found")
        order_items = []
        total_price = Decimal("0.00")
        for item in order_data.order_items:
            product = ProductService.get_product(db, item.product_id)
            if not product:
                raise ValueError(f"Product {item.product_id} not found")
            total_price += product.price * item.quantity
            order_items.append(
                OrderItem(
                    product_id=product.id,
                    price_at_order=product.price,
                    quantity=item.quantity,
                )
            )
        order = Order(
            client_id=client.id,
            order_items=order_items,
            total_price=total_price
        )
        db.add(order)
        print(order.__dict__)
        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def read_order(client_id: int, db: Session):
        order_list = db.query(Order).filter(Order.client_id == client_id).all()
        return order_list
