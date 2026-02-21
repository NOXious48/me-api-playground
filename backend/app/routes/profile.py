from fastapi import APIRouter, HTTPException
from app.db import profile_collection
from app.models import Profile

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.post("/", status_code=201)
def create_or_update_profile(profile: Profile):
    # Single-profile design (portfolio-style)
    profile_collection.delete_many({})
    profile_collection.insert_one(profile.dict())
    return {"message": "Profile stored successfully"}


@router.get("/")
def get_profile():
    profile = profile_collection.find_one({}, {"_id": 0})
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
