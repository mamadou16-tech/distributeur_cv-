"""Modèle Company : base de données centralisée des entreprises."""
from datetime import datetime

from sqlalchemy import Boolean, DateTime, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Company(Base):
    """Une entreprise cible, ajoutée manuellement ou découverte par l'IA.

``has_active_offer`` distingue les entreprises qui publient réellement
    une offre de celles visées par une candidature spontanée.
    """

__tablename__ = "companies"

id: Mapped[int] = mapped_column(primary_key=True)
name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
country: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
city: Mapped[str | None] = mapped_column(String(100), nullable=True)
sector: Mapped[str | None] = mapped_column(String(150), nullable=True, index=True)
description: Mapped[str | None] = mapped_column(Text, nullable=True)
website: Mapped[str | None] = mapped_column(String(500), nullable=True)
contact_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
hr_contacts: Mapped[dict | None] = mapped_column(JSON, nullable=True)
has_active_offer: Mapped[bool] = mapped_column(Boolean, default=False)
source: Mapped[str | None] = mapped_column(String(255), nullable=True)
last_verified_at: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True), nullable=True
)
created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now()
)
updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
)

opportunities = relationship(
        "Opportunity", back_populates="company", cascade="all, delete-orphan"
    )
