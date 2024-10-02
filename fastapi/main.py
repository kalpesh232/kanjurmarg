from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException
from typing import Union, Annotated
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 1 from Kalpesh"}

@app.get("/hello")
async def hello():
    return {"message": "Hey ! Hi  World  from Kalpesh"}

@app.get("/item/{item}")
def path_fun(item):
    var_name = {"path_variable" :  item}
    return var_name

# @app.get("/query")
# def query_fun(name:str, roll_no:int):
#     var_name = {"Name" :  name, "roll_no" : roll_no}
#     return var_name

# @app.get("/query")
# def query_fun(name:str, roll_no:Union[int,None]=None):
#     var_name = {"Name" :  name, "roll_no" : roll_no}
#     return var_name

@app.get("/query")
def query_fun(name:str, roll_no:Union[str,None]=Query(default=None, min_length=3, max_length=3)):
    var_name = {"Name" :  name, "roll_no" : roll_no}
    return var_name

class choose_Name(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: choose_Name):
    return model_name

# --------- Request Body

from pydantic import BaseModel

# class scheema(BaseModel):
#     name : str
#     age : int
#     salary : int

class scheema(BaseModel):
    name : str
    age : int 
    salary : int

@app.post("/items/")
async def req_body(item: scheema):
    return item

# ---------- Form Data

@app.post("/form/data")
# async def form_data(username : Annotated[str, Form()]):
# async def form_data(username : str):
async def form_data(username : str = Form()):
    return ({"UserName" : username})

# ---------- File Upload 

@app.post("/file/bytes")
async def file_bytes(file : bytes = File()):
    return("File Bytes : ", len(file))

@app.post("/file/info")
async def file_info(file : UploadFile):
    return ("File Info : ", file)

# ---------- Handling Errors

@app.get("/handeling/error")
async def handling_error(item : int):
    if item == 2 :
        return HTTPException(status_code=400, detail="Item should be not equal to 2 ! Try another value")
    return{"item : ", item}