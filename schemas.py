from pydantic import BaseModel


class TodoCreate(BaseModel):
    text:  str

class TodoUpdate(BaseModel):
    text: str


class TodoDelete(BaseModel):
    id: int