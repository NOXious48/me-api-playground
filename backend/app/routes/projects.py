from fastapi import APIRouter, HTTPException
from app.db import projects_collection

router = APIRouter(tags=["Projects"])

@router.get("/projects")
def list_projects():
    return [
        {
            "slug": p["slug"],
            "title": p["title"],
            "subtitle": p["subtitle"]
        }
        for p in projects_collection.find({}, {"_id": 0})
    ]

@router.get("/projects/{slug}")
def get_project(slug: str):
    project = projects_collection.find_one({"slug": slug}, {"_id": 0})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
