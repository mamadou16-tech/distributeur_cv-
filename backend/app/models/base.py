"""Base déclarative commune à tous les modèles."""
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Classe de base SQLAlchemy 2.0 pour tous les modèles du projet."""
