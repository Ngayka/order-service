from pydantic import BaseModel

from order_service.schemas.product import ProductListSchema


class OrderItemCreateSchema(BaseModel):
    product_id: int
    quantity: int = 1


class OrderItemReadSchema(BaseModel):
    product: ProductListSchema
    quantity: int
    price_at_order: float


class OrderCreateSchema(BaseModel):
    client_id: int
    order_items: list[OrderItemCreateSchema]


class OrderReadSchema(BaseModel):
    id: int
    client_id: int
    order_items: list[OrderItemReadSchema]
    total_price: float
