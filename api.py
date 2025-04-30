from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import User
from typing import List
import os

app = FastAPI()

MONGO_URI = "mongodb+srv://jeganrpalani:CBPw6ueTGchtJZDs@cluster0.y0lddgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["chikku"]
collection = db["user"]

@app.post("/users/")
def create_user(user: User):
    result = collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

@app.get("/users/", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Exclude _id for clean response
    return users

@app.get("/users/{name}", response_model=User)
def get_user_by_name(name: str):
    user = collection.find_one({"name": name}, {"_id": 0})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")