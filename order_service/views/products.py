from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from order_service.db.session import get_db
from order_service.models import Product
from order_service.schemas.product import ProductCreateSchema, ProductReadSchema
from order_service.service.product_service import ProductService

router = APIRouter()


@router.post("/products", response_model=ProductReadSchema)
def create_product(product: ProductCreateSchema, db: Session = Depends(get_db)):
    return ProductService.create(product, db)


@router.get("/products", response_model=List[ProductReadSchema])
def get_products(db: Session = Depends(get_db)):
    return db.scalars(select(Product)).all()


@router.get("/products/{product_id}", response_model=ProductReadSchema)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return ProductService.get_product(db, product_id)
