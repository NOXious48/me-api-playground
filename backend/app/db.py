import os
from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI environment variable not set")

client = MongoClient(MONGODB_URI)
db = client["me_api"]

profile_collection = db["profile"]
projects_collection = db["projects"]
