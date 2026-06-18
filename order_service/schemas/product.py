from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductCreateSchema(ProductBase):
    pass


class ProductListSchema(ProductBase):
    id: int

