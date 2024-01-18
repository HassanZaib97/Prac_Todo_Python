from pydantic import BaseModel


class TodoCreate(BaseModel):
    title:  str
    description: str

class TodoUpdate(BaseModel):
    title:  str
    description: str


class TodoDelete(BaseModel):
    id: int


