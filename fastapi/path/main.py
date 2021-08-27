from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


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


@path.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
