from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    topic: str


class Book(BookCreate):
    id: int


class CreateTable(BaseModel):
    create: bool
