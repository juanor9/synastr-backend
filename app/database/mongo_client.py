from pymongo import MongoClient
import os

MONGO_URI = os.getenv("DATABASE_URL", "mongodb+srv://juan:P2drmvyxm59Bh1vS@caikei.i4nc3u3.mongodb.net/synastr-dev")

client = MongoClient(MONGO_URI)
db = client["synastr-dev"]

users_collection = db["users"]
messages_collection = db["messages"]
compatibility_collection = db["compatibility"]
reports_collection = db["reports"]
