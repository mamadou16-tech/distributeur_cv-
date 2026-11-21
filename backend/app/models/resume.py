"""Modèle Resume : versions de CV et profil structuré extrait par l'IA."""
from datetime import datetime

from sqlalchemy import Boolean, DateTime, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Resume(Base):
    """Une version de CV (ex: orientation IA, industrie, biotech...).

``parsed_profile`` contiendra la fiche structurée produite par le
    Resume Analyzer Agent (compétences, formations, expériences...),
    corrigeable par l'utilisateur (Phase 2).
    """

__tablename__ = "resumes"

id: Mapped[int] = mapped_column(primary_key=True)
label: Mapped[str] = mapped_column(String(120), index=True)
original_filename: Mapped[str] = mapped_column(String(255))
file_path: Mapped[str] = mapped_column(String(500))
raw_text: Mapped[str | None] = mapped_column(Text, nullable=True)
parsed_profile: Mapped[dict | None] = mapped_column(JSON, nullable=True)
is_active: Mapped[bool] = mapped_column(Boolean, default=True)
created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now()
)
updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
)
