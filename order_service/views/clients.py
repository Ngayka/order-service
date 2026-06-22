from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from order_service.db.session import get_db
from order_service.schemas.client import ClientCreateSchema, ClientReadSchema
from order_service.service.client_service import ClientService

router = APIRouter()


@router.post("/clients", response_model=ClientReadSchema)
def create_order(client: ClientCreateSchema, db: Session = Depends(get_db)):
    return ClientService.create(db, client)
