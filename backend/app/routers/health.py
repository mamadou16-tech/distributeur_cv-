"""Endpoints de santé et diagnostic de la base."""
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/api", tags=["health"])

@router.get("/health")
def health(db: Session = Depends(get_db)) -> dict:
    """Vérifie que l'API répond ET que PostgreSQL est joignable."""
    db.execute(text("SELECT 1"))
    return {
        "status": "ok",
        "database": "connected",
        "app_env": "development",
    }
