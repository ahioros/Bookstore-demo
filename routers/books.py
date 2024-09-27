from crud.book import creation_book, delete_book, read_books, update_book
from fastapi import APIRouter
from models.book import Book, BookCreate

router = APIRouter(
    prefix="/books", tags=["books"], responses={404: {"description": "Ops! Not found"}}
)


@router.get("/")
async def root():
    if not read_books():
        return {"message": "Table empty"}
    return read_books()


@router.get("/{book_id}")
async def get_book_endpoint(book_id: int):
    return read_books(book_id)


@router.post("/")
async def create_book_endpoint(book: BookCreate):
    book_id = creation_book(book)
    return {"id": book_id, **book.dict()}


@router.put("/{book_id}")
async def update_book_endpoint(book: Book):
    if update_book(book):
        return {"message": "Book updated"}


@router.delete("/{book_id}")
async def delete_book_endpoint(book_id: int):
    if delete_book(book_id):
        return {"message": "Book deleted"}
