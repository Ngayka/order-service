from sqlalchemy.orm import Session

from order_service.schemas.order import OrderCreateSchema
from order_service.service.product_service import ProductService


class OrderService:
    @staticmethod
    def create(order_data: OrderCreateSchema, db: Session):
        total_price = 0
        for item in order_data.order_items:
            product = ProductService.get_product(db, item.product_id)
            total_price += product.price * item.quantity
