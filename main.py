from fastapi import FastAPI
from pydantic import EmailStr, BaseModel


import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "hello",
    }


@app.get("/items")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@app.get("/items/latest")
def get_latest_item():
    return {"Item": {"id": "0", "name": "latest"}}


@app.get("/items{item_id}")
def get_item_by_id(item_id: int):
    return {
        "Item": {
            "id": item_id,
        },
    }


@app.get("/hello")
def hello(name: str = "User"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.post("/calc")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)