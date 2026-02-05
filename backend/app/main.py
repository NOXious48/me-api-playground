from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.search import router as search_router
from app.projects import router as projects_router
from app.profile import router as profile_router

app = FastAPI(title="Pushp Raj Panth API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ok for portfolio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(profile_router)
app.include_router(projects_router)
app.include_router(search_router)

# Health check
@app.get("/")
def root():
    return {"status": "API is running"}
