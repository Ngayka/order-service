from sqlalchemy.orm import Session

from order_service.models.client import Client
from order_service.schemas.client import ClientCreateSchema


class ClientService:
    @staticmethod
    def create(db: Session, client_data: ClientCreateSchema):
        client = Client(name=client_data.name,
                        email=client_data.email)

        db.add(client)
        db.commit()
        db.refresh(client)

        return client
