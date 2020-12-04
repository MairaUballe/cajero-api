from fastapi import FastAPI
from db.user_db import database_users
from fastapi import HTTPException
from db.user_db import UserInDB

api = FastAPI()

@api.get("/")           # GET / HTTP/1.1 (lado del cliente) 
async def root():
    return {"message": "Hello FastAPI"}

@api.get("/users")           # GET /users HTTP/1.1 (lado del cliente) 
async def users():
    return {"message": database_users}

@api.get("/users/{username}")           # GET /users HTTP/1.1 (lado del cliente) 
async def get_user_by_username(username : str):
    if username in database_users:
        return {"message": database_users[username]}
    raise HTTPException(status_code=404, detail="¡El usuario no existe!")

@api.post("/users/")
async def create_user(user : UserInDB):
    database_users[user.username] = user
    return user

@api.delete("/users/")
async def delete_user(user : UserInDB):
    del database_users[user.username]
    return user

@api.put("/users/")
async def update_user(user : UserInDB):
    database_users[user.username] = user
    return user