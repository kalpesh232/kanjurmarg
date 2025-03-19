"""
1. Data validation
2. Auto Documentation
3. Auto complete & code suggestions

pip install fastapi
pip install uvicorn
uvicorn techwithtim:app --reload 
"""

from fastapi import FastAPI, Path, Query, HTTPException,status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

inventory = {
    1: {"name": "Milk", "price": 3.99, "brand": "Regular"},
    2: {"name": "Bread", "price": 2.49, "brand": "Fresh Bakes"},
    3: {"name": "Eggs", "price": 4.99, "brand": "Farm Fresh"},
    4: {"name": "Butter", "price": 5.49, "brand": "Golden Dairy"},
    5: {"name": "Cheese", "price": 6.99, "brand": "Cheddar Best"}
}

class Item(BaseModel):
        name : str
        price :float
        brand : Optional[str] = None

class UpdateItem(BaseModel):
        name : Optional[str] = None
        price :Optional[float] = None
        brand : Optional[str] = None
    
@app.get("/")
def home():
    return {"msg" : "Test"}

@app.get("/about")
def about():
    return {"msg" : "About"}

# @app.get("/get_item/{item_id}")
# def get_item(item_id:int):
#     return inventory[item_id]

# @app.get("/get_item/{item_id}/{item_name}")
# def get_item(item_id:int,item_name:str ):
#     return inventory[item_id]

# @app.get("/get_item/{item_id}")
# def get_item(item_id:int=Path(..., description="The ID of Item you would like to view")):
#     return inventory[item_id]

@app.get("/get_item/{item_id}")
def get_item(item_id:int=Path(..., description="The ID of Item you would like to view",gt=0, lt=10)):
    if item_id not in inventory:
         raise HTTPException(status_code=404, detail="Item with that ID Not Found")
    return inventory[item_id]

# @app.get("/get_by_name")
# def get_by_name(item_name:str):
#     for item_id in inventory:
#         print(f'{inventory[item_id]["name"]}=={item_name}')
#         if inventory[item_id]["name"] == item_name :
#             print("*"*25)
#             return inventory[item_id]
#     return {"Data":"Not Found"}

# @app.get("/get_by_name")                                      # Implicitly allows None, but str
# def get_by_name(item_name:str = None):
#     for item_id in inventory:
#         print(f'{inventory[item_id]["name"]}=={item_name}')
#         if inventory[item_id]["name"] == item_name :
#             print("*"*25)
#             return inventory[item_id]
#     return {"Data":"Not Found"}


# @app.get("/get_by_name")                                     # Explicitly states that item_name can be str or None
# def get_by_name(item_name:Optional[str] = None):
#     for item_id in inventory:
#         print(f'{inventory[item_id]["name"]}=={item_name}')
#         if inventory[item_id]["name"] == item_name :
#             print("*"*25)
#             return inventory[item_id]
#     return {"Data":"Not Found"}


# @app.get("/get_by_name")                             # "query","test" required                                  
# def get_by_name(*,item_name:Optional[str] = None, test:int):
#     for item_id in inventory:
#         print(f'{inventory[item_id]["name"]}=={item_name}')
#         if inventory[item_id]["name"] == item_name :
#             print("*"*25)
#             return inventory[item_id]
#     return {"Data":"Not Found"}

# --------- query & Path Parameter together

@app.get("/get_by_name/{item_name}")                                                            
def get_by_name(*,item_id : int, item_name:Optional[str] = None, test:int):
    for item_idx in inventory:
        print(f'{inventory[item_idx]["name"]}=={item_name}')
        if inventory[item_idx]["name"] == item_name :
            print("*"*25)
            return inventory[item_idx]
    raise HTTPException(status_code=404, detail="Item Name with that ID Not Found")

@app.post("/create_item/{item_id}")
def create_item(item_id:int, item:Item):
     if item_id in inventory:
          raise HTTPException(status_code=400, detail="Item with that ID Already Exist")
     print('item : ',item)
     inventory[item_id] = item
     return inventory

@app.put("/update_item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
     if item_id not in inventory:
          raise HTTPException(status_code=404, detail="Item with that ID Not Found")
     if item.name != None:
          inventory[item_id]['name'] = item.name
     if item.brand != None:
          inventory[item_id]['brand'] = item.brand
     if item.price != None:
          inventory[item_id]['price'] = item.price

     return inventory

# @app.delete("/delete_item/{item_id}")
# def delete_item(item_id:int):
#      if item_id not in inventory:
#           return {"Error" : "Item ID Doest Not  Exist"}
#     #  inventory.pop(item_id)
#      del inventory[item_id]
#      return inventory

@app.delete("/delete_item")
def delete_item(item_id:int=Query(...,description="Item ID is Reqired",lt=5, gt=1 )):
     if item_id not in inventory:
          raise HTTPException(status_code=404, detail="Item with that ID Not Found")
    #  inventory.pop(item_id)
     del inventory[item_id]
     return inventory