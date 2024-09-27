import os
import sqlite3

from models.book import Book, BookCreate


def create_connection():
    connection = sqlite3.connect(os.environ["DATABASE"])
    return connection


def create_table() -> None:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books \
                (id INTEGER PRIMARY KEY AUTOINCREMENT,\
                title TEXT, author TEXT, topic TEXT)"
    )
    connection.commit()
    connection.close()


def creation_book(book: BookCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO books \
                (title, author, topic) VALUES (?,?,?)",
        (book.title, book.author, book.topic),
    )
    connection.commit()
    connection.close()


def fill_table():
    creation_book(
        BookCreate(title="Cien años de soledad", author="Gabriel Garcia M", topic="Fantasia")
    )
    creation_book(
        BookCreate(
            title="El coronel no tiene quien le escriba",
            author="Gabriel Garcia M",
            topic="Fantasia",
        )
    )
    creation_book(BookCreate(title="IT", author="Stephen King", topic="Terror"))
    creation_book(BookCreate(title="The Mist", author="Stephen King", topic="Terror"))


def read_books() -> list[Book]:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    Books = cursor.fetchall()
    connection.close()
    booklist = [Book(id=book[0], title=book[1], author=book[2], topic=book[3]) for book in Books]
    return booklist


def update_book(book: Book) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE books SET title =?, author =?, topic =? WHERE id =?",
        (book.title, book.author, book.topic, book.id),
    )
    connection.commit()
    return True


def delete_book(book_id: str) -> bool:
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id =?",
        (book_id,),
    )
    connection.commit()
    return True
