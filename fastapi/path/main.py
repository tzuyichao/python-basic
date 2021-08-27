from fastapi import FastAPI

path = FastAPI()


@path.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"id": item_id}


@path.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@path.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
