from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: str
    email: EmailStr


class ClientCreateSchema(ClientBase):
    pass


class ClientReadSchema(ClientBase):
    id: int
