from sqlalchemy.orm import Session

from order_service.models import Product


class ProductService:
    @staticmethod
    def get_product(db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()
