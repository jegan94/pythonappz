from flask import Flask, jsonify, request
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import User
from typing import List

app = Flask(__name__)

# app = FastAPI()

MONGO_URI = "mongodb+srv://jeganrpalani:CBPw6ueTGchtJZDs@cluster0.y0lddgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["chikku"]
collection = db["user"]

login_res = [
    {'status': '200', 'message': 'Login successfully', 'username': 'Test', 'mobile': 9876543210,
     'email': 'test@gmail.com'}
]


@app.get("/users/", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Exclude _id for clean response
    return users

@app.post("/users/")
def create_user(user: User):
    result = collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/login")
def login():
    return login_res

@app.route('/newlogin', methods=['POST'])
def newlogin():
    login_res.append(request.get_json())
    return 'Registration successfully', 200
