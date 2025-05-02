# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# login_res = [
#     {'status': '200', 'message': 'Login successfully', 'username': 'Test', 'mobile': 9876543210,
#      'email': 'test@gmail.com'}
# ]
#
# @app.route("/")
# def hello_world():
#     return "Hello world"
#
#
# @app.route("/login")
# def login():
#     return login_res
#
# @app.route('/newlogin', methods=['POST'])
# def newlogin():
#     login_res.append(request.get_json())
#     return 'Registration successfully', 200

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

# Connect to MongoDB Atlas
MONGO_URI = "mongodb+srv://jeganrpalani:CBPw6ueTGchtJZDs@cluster0.y0lddgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["chikku"]
collection = db["user"]

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int

@app.get("/")
async def root():
    return {"message": "Hello World1"}

@app.get("/user/", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Exclude _id for clean response
    return users

@app.get("/users", response_model=List[User])
def get_all_users():
    users = list(collection.find({}, {"_id": 0}))
    return users

# Create user (POST)
@app.post("/new_user")
def create_user(user: User):
    result = collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

# Get one user by name (GET)
@app.get("/users/{name}", response_model=User)
def get_user_by_name(name: str):
    user = collection.find_one({"name": name}, {"_id": 0})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
