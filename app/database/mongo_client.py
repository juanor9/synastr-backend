from pymongo import MongoClient
from app.config.settings import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client["synastr-dev"]

users_collection = db["users"]
messages_collection = db["messages"]
compatibility_collection = db["compatibility"]
reports_collection = db["reports"]

