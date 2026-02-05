from fastapi import APIRouter, HTTPException
from app.db import profile_collection, projects_collection

router = APIRouter(prefix="/search", tags=["Search"])


# --------------------------------------------------
# 1️⃣ List technical skills
# --------------------------------------------------
@router.get("/skills")
def list_skills():
    profile = profile_collection.find_one({}, {"_id": 0})
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.get("technical_skills", {})


# --------------------------------------------------
# 2️⃣ Search CV-level project summaries (profile projects)
# --------------------------------------------------
@router.get("/profile-projects")
def search_profile_projects(keyword: str):
    profile = profile_collection.find_one({}, {"_id": 0})
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    keyword = keyword.lower()

    return [
        p for p in profile.get("projects", [])
        if keyword in p.get("project_title", "").lower()
        or keyword in p.get("description", "").lower()
    ]


# --------------------------------------------------
# 3️⃣ Global search across profile + project pages
# --------------------------------------------------
@router.get("/")
def full_text_search(q: str):
    q = q.lower()
    results = []

    profile = profile_collection.find_one({}, {"_id": 0})

    # ---- Search experience ----
    if profile:
        for exp in profile.get("experience", []):
            haystack = (exp.get("role", "") + exp.get("organization", "")).lower()
            if q in haystack:
                results.append({
                    "type": "experience",
                    "title": exp.get("role"),
                    "data": exp
                })

        # ---- Search profile project summaries ----
        for project in profile.get("projects", []):
            if q in project.get("description", "").lower():
                results.append({
                    "type": "profile_project",
                    "title": project.get("project_title"),
                    "data": project
                })

    # ---- Search full project pages (VREyeSAM / SSBC) ----
    for project in projects_collection.find({}, {"_id": 0}):
        text = (
            " ".join(project.get("overview", [])) +
            " ".join(project.get("results", {}).get("highlights", []))
        ).lower()

        if q in text:
            results.append({
                "type": "project_page",
                "title": project.get("title"),
                "slug": project.get("slug")
            })

    return results
