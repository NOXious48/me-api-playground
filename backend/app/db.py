from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)
db = client["me_api"]

profile_collection = db["profile"]
projects_collection = db["projects"]
