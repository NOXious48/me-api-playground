from fastapi import APIRouter, HTTPException
from app.db import projects_collection

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/")
def list_projects():
    """
    List all full project pages.
    Returns only metadata needed for the main page.
    """
    projects = projects_collection.find({}, {"_id": 0})
    return [
        {
            "slug": p["slug"],
            "title": p["title"],
            "subtitle": p["subtitle"]
        }
        for p in projects
    ]


@router.get("/{slug}")
def get_project(slug: str):
    """
    Fetch a single full project page by slug.
    Used by project.html.
    """
    project = projects_collection.find_one({"slug": slug}, {"_id": 0})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project
