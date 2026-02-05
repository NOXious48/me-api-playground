from fastapi import APIRouter, HTTPException
from app.db import profile_collection, projects_collection

router = APIRouter(tags=["Search"])

# --------------------------------------------------
# 1️⃣ List technical skills
# --------------------------------------------------
@router.get("/skills")
def list_skills():
    profile = profile_collection.find_one({})
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.get("technical_skills", {})


# --------------------------------------------------
# 2️⃣ Search SHORT project summaries (CV-level)
# --------------------------------------------------
@router.get("/profile/projects")
def search_profile_projects(keyword: str):
    profile = profile_collection.find_one({})
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    keyword = keyword.lower()

    return [
        p for p in profile.get("projects", [])
        if keyword in p.get("project_title", "").lower()
        or keyword in p.get("description", "").lower()
    ]


# --------------------------------------------------
# 3️⃣ List FULL project pages (VREyeSAM, SSBC)
# --------------------------------------------------
@router.get("/projects")
def list_project_pages():
    return [
        {
            "slug": p["slug"],
            "title": p["title"],
            "subtitle": p["subtitle"]
        }
        for p in projects_collection.find({}, {"_id": 0})
    ]


# --------------------------------------------------
# 4️⃣ Get FULL project page by slug
# --------------------------------------------------
@router.get("/projects/{slug}")
def get_project_page(slug: str):
    project = projects_collection.find_one({"slug": slug}, {"_id": 0})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


# --------------------------------------------------
# 5️⃣ Global search across profile + project pages
# --------------------------------------------------
@router.get("/search")
def full_text_search(q: str):
    q = q.lower()
    results = []

    profile = profile_collection.find_one({})

    if profile:
        # Profile project summaries
        for project in profile.get("projects", []):
            if q in project.get("description", "").lower():
                results.append({
                    "type": "profile_project",
                    "title": project.get("project_title"),
                    "data": project
                })

        # Experience
        for exp in profile.get("experience", []):
            haystack = (exp.get("role", "") + exp.get("organization", "")).lower()
            if q in haystack:
                results.append({
                    "type": "experience",
                    "title": exp.get("role"),
                    "data": exp
                })

    # Full project pages
    for project in projects_collection.find({}, {"_id": 0}):
        if q in project.get("description", "").lower():
            results.append({
                "type": "project_page",
                "title": project.get("title"),
                "slug": project.get("slug")
            })

    return results
