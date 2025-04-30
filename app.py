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

from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB connection
MONGO_URI = "mongodb+srv://jeganrpalani:CBPw6ueTGchtJZDs@cluster0.y0lddgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["users"]

@app.get("/")
def home():
    return {"message": "Hello from FastAPI with MongoDB"}

@app.post("/add_user/")
def add_user(user: dict):
    collection.insert_one(user)
    return {"status": "User added"}
