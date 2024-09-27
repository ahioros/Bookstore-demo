import base64
import os

import uvicorn
from fastapi import FastAPI

from crud.book import create_table, fill_table
from routers import books

app = FastAPI(debug=True)

app.include_router(books.router)


@app.get("/secret")
async def get_token():
    return {
        "SECRET_TOKEN_ENCODE": base64.b64encode(os.environ["SECRET_TOKEN"].encode("ascii")),
        "SECRET_TOKEN_DECODE": os.environ["SECRET_TOKEN"],
    }


@app.get("/")
async def read_root():
    return {"message": "Welcome to the CRUD API example!"}


if __name__ == "__main__":
    if not os.environ["DATABASE"] or not os.environ["SECRET_TOKEN"]:
        database = True
        raise ValueError(
            "DATABASE environment variable not set, must: export DATABASE=bookstore.db, \n   SECRET_TOKEN environment variable not set, must: export SECRET_TOKEN=SUPER$ECRET_P4SSW0RD"
        )

    if not os.path.exists(os.environ["DATABASE"]):
        create_table()
        fill_table()
    uvicorn.run(app, host="0.0.0.0", port=8000)
