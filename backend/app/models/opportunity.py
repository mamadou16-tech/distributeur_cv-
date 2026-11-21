"""Modèle Opportunity : offres de stage/emploi détectées ou saisies."""
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Opportunity(Base):
    """Une offre (stage, emploi, alternance) rattachée à une entreprise.

``required_skills`` : liste JSON extraite par l'Opportunity Agent.
    ``source_url`` + ``posted_at`` garantissent la traçabilité
    (aucune offre inventée).
    """

__tablename__ = "opportunities"

id: Mapped[int] = mapped_column(primary_key=True)
company_id: Mapped[int] = mapped_column(
    ForeignKey("companies.id", ondelete="CASCADE"), index=True
)
title: Mapped[str] = mapped_column(String(255))
contract_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
description: Mapped[str | None] = mapped_column(Text, nullable=True)
required_skills: Mapped[list | None] = mapped_column(JSON, nullable=True)
location: Mapped[str | None] = mapped_column(String(255), nullable=True)
source_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)
posted_at: Mapped[date | None] = mapped_column(Date, nullable=True)
is_active: Mapped[bool] = mapped_column(Boolean, default=True)
fetched_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now()
)

company = relationship("Company", back_populates="opportunities")
