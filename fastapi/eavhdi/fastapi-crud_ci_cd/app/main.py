from fastapi import FastAPI

app = FastAPI()

items = []

@app.post('/items')
def create_item(item:str):
    items.append(item)

@app.get('/items')
def get_items():
    return items

@app.delete('/items/{index}')
def del_item(index:int):
    items.pop(index)
    return {"message" : "Item Deleted"}