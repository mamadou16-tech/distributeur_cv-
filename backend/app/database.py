"""Moteur SQLAlchemy et fabrique de sessions."""
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import settings

engine = create_engine(settings.sqlalchemy_url, pool_pre_ping=True, echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

def get_db() -> Generator[Session, None, None]:
    """Dépendance FastAPI : une session par requête, fermée automatiquement."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
