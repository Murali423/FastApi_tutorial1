from enum import Enum
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/",description="base root of the application")
async def root():
    return {"message":"Hello world this is my first fastapi program"}

@app.post("/")
async def post():
    return {"message":"Hello from post"}

@app.put("/")
async def put():
    return {"message":"i am from put request"}

@app.get("/item")
async def list_route():
    return {"meassage":"This is from the list of routes"}

# @app.get("/item")
# async def list_route1():
#     return {"meassage":"This is from the list of routes"}

@app.get("/item/{item_id}")
async def get_item(item_id: int):
    return {"item_id":item_id}


@app.get("/user/me")
async def get_user():
    return {"message":"this is the current user"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegtables = "vegtables"
    dairy = "dairy"

@app.get("/food/{food_item}")
async def get_food(food_item:FoodEnum):
    if food_item == FoodEnum.vegtables:
        return {"food_name":food_item,
                "message": "You are healthy"
                }
    if food_item.value == "fruits":
        return {"food_name":food_item,
                "message": "You are healthy with little sweetness"
                }
    return {"food_name":food_item,"message":"I like choclate milk"}

fake_item_db = [{"item_name":"Foo"},{"item_name":"Boo"},{"item_name":"buzz"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_item_db[skip:skip+limit]

@app.get("/items/{item_id}")
async def get_item(item_id : str,q: Optional[str]=None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item_id":item_id}

@app.get("/itemss/{item_id}")
async def get_item(item_id : str,q: str | None = None, short : bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":"This is quary parameter has been added to the item"})
    if not short:
        item.update({"description":"This is a small descritpion"})
    return item

@app.get("/user/{user_id}/item/{item_id}")
async def get_user_item(user_id : str, item_id : str, q : str | None = None, short : bool =False):
    item = {"item_id":item_id,"owner":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"short":"little short description"})
    return item