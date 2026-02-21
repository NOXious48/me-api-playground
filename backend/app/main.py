from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.profile import router as profile_router
from app.routes.projects import router as projects_router
from app.routes.search import router as search_router

app = FastAPI(title="Pushp Raj Panth API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile_router)
app.include_router(projects_router)
app.include_router(search_router)

@app.get("/")
def root():
    return {"status": "API running locally"}
