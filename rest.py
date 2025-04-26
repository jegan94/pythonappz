from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace with your actual MongoDB URI
uri = "mongodb+srv://jeganrpalani:CBPw6ueTGchtJZDs@cluster0.y0lddgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# uri = "mongodb+srv://jeganrpalani:CBPw6ueTGchtJZDs@cluster0.y0lddgy.mongodb.net/?appName=Cluster0"

# Create a MongoClient with the Server API version 1
client = MongoClient(uri, server_api=ServerApi('1'))

# Try to ping the MongoDB server
try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed:", e)
