from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductCreateSchema(ProductBase):
    pass


class ProductReadSchema(ProductBase):
    id: int


