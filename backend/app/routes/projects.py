from fastapi import APIRouter, HTTPException
from app.db import projects_collection

router = APIRouter(prefix="/projects", tags=["Projects"])


# --------------------------------------------------
# List all project pages (for index.html)
# --------------------------------------------------
@router.get("/")
def list_projects():
    return list(
        projects_collection.find(
            {},
            {"_id": 0, "slug": 1, "title": 1, "subtitle": 1}
        )
    )


# --------------------------------------------------
# Get full project page by slug
# --------------------------------------------------
@router.get("/{slug}")
def get_project(slug: str):
    project = projects_collection.find_one({"slug": slug}, {"_id": 0})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
