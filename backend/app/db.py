import os
from pymongo import MongoClient
import certifi  # <--- Import this

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    # Fallback for local testing if env var is missing
    MONGODB_URI = "mongodb://localhost:27017" 

# Add tlsCAFile=certifi.where() to fix the handshake error
client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

db = client["me_api"]

profile_collection = db["profile"]
projects_collection = db["projects"]