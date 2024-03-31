from enum import Enum
from fastapi import FastAPI


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

