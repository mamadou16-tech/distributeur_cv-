"""Point d'entrée FastAPI de CV Distributor."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routers.health import router as health_router

# Création des tables au démarrage (Phase 1 ; Alembic viendra plus tard).
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CV Distributor",
    description="Agent intelligent de distribution de CV",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend React (Phase 7)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
