from sqlalchemy.orm import Session

from order_service.models import Product
from order_service.schemas.product import ProductCreateSchema


class ProductService:
    @staticmethod
    def get_product(db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def create(product_data: ProductCreateSchema, db: Session):
        product = Product(name=product_data.name,
                          description=product_data.description,
                          price=product_data.price)

        db.add(product)
        db.commit()
        db.refresh(product)

        return product


