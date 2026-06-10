from fastapi import FastAPI
from models import User
from middelware import customTimeMiddelware
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(customTimeMiddelware)

users_db = []

@app.post("/users/")
def create_user(user:User):
    print("*" *25, users_db)
    if any(u.email == user.email for u in users_db) :
        return JSONResponse(
            status_code=400,
            content={"status" : "Fail", "message" : "User Already Exist !"}
        )
    else:
        users_db.append(user)
        return JSONResponse(
            status_code=201,
            content={"status" : "success", "message" : "User Created Successfully !"}
        )
    
@app.get("/users/")
def users_list():
    return users_db