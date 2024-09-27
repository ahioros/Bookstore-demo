import os

from app import app
from crud.book import create_table, creation_book
from fastapi.testclient import TestClient
from models.book import BookCreate

client = TestClient(app)

os.environ["DATABASE"] = "TEST_DATABASE.db"
os.environ["SECRET_TOKEN"] = "SUPER_SECRETPASSW0RD"


def __delete_database():
    if os.path.exists(os.environ["DATABASE"]):
        os.remove(os.environ["DATABASE"])


def test_secret():
    response = client.get("/secret")
    assert response.status_code == 200
    assert response.json() == {
        "SECRET_TOKEN_ENCODE": "U1VQRVJfU0VDUkVUUEFTU1cwUkQ=",
        "SECRET_TOKEN_DECODE": "SUPER_SECRETPASSW0RD",
    }


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the CRUD API example!"}


def test_get_books():
    create_table()
    creation_book(
        BookCreate(title="Cien años de soledad", author="Gabriel Garcia M", topic="Fantasia")
    )

    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "Cien años de soledad",
            "author": "Gabriel Garcia M",
            "topic": "Fantasia",
        }
    ]

    __delete_database()
