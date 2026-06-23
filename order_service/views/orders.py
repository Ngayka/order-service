from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from order_service.db.session import get_db
from order_service.schemas.order import OrderCreateSchema, OrderReadSchema
from order_service.service.order_service import OrderService


router = APIRouter()


@router.post("/orders", response_model=OrderReadSchema)
def create_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    return OrderService.create(order, db)


@router.get("/orders", response_model=list[OrderReadSchema])
def order_list(client_id: int, db: Session = Depends(get_db)):
    return OrderService.read_order(client_id, db)