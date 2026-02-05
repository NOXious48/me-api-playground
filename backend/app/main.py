from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.search import router as search_router
from app.routes.projects import router as projects_router
from app.routes.profile import router as profile_router
from app.routes.health import router as health_router

app = FastAPI(title="Pushp Raj Panth API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for portfolio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# ROUTERS
# ---------------------------
app.include_router(health_router)
app.include_router(profile_router)
app.include_router(projects_router)
app.include_router(search_router)
