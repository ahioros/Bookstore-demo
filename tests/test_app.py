import sys
import os
import sqlite3

# add the root dir of the project
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_path)  # noqa E402
from app import Book, read_book  # noqa  E402

# add the root dir of the project
# root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, root_path)
# from app import Book, read_book


def test_read_book():
    # Create conecction to db in memory
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create the table and insert the books
    cursor.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, topic TEXT)"
    )
    cursor.execute(
        "INSERT INTO books (title, author, topic) VALUES ('Cien años de soledad', 'Gabriel Garcia M', 'Fantasía')"
    )
    cursor.execute(
        "INSERT INTO books (title, author, topic) VALUES ('El coronel no tiene quien le escriba', 'Gabriel Garcia M', 'Fantasía')"
    )
    cursor.execute(
        "INSERT INTO books (title, author, topic) VALUES ('IT', 'Stephen King', 'Terror')"
    )
    cursor.execute(
        "INSERT INTO books (title, author, topic) VALUES ('The Mist', 'Stephen King', 'Terror')"
    )

    conn.commit()

    # execute the function to test
    result = read_book()

    # the expected result
    expected_result = [
        Book(
            id=1,
            title="Cien años de soledad",
            author="Gabriel Garcia M",
            topic="Fantasía",
        ),
        Book(
            id=2,
            title="El coronel no tiene quien le escriba",
            author="Gabriel Garcia M",
            topic="Fantasía",
        ),
        Book(id=3, title="IT", author="Stephen King", topic="Terror"),
        Book(id=4, title="The Mist", author="Stepehen King", topic="Terror"),
    ]
    assert result == expected_result

    # close conecction to the db
    cursor.close()
    conn.close()
