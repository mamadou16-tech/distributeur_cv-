"""Modèle Campaign : paramètres d'une campagne de recherche."""
from datetime import date, datetime

from sqlalchemy import Date, DateTime, Integer, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Campaign(Base):
    """Une campagne de candidature (secteurs, pays, limites d'envoi...).

``send_mode`` : manual | semi_auto | auto.
    """

__tablename__ = "campaigns"

id: Mapped[int] = mapped_column(primary_key=True)
name: Mapped[str] = mapped_column(String(255))
contract_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
target_sectors: Mapped[list | None] = mapped_column(JSON, nullable=True)
target_countries: Mapped[list | None] = mapped_column(JSON, nullable=True)
target_cities: Mapped[list | None] = mapped_column(JSON, nullable=True)
required_skills: Mapped[list | None] = mapped_column(JSON, nullable=True)
stage_duration_months: Mapped[int | None] = mapped_column(String(20), nullable=True)
availability_date: Mapped[date | None] = mapped_column(Date, nullable=True)
send_mode: Mapped[str] = mapped_column(String(20), default="manual")
daily_send_limit: Mapped[int] = mapped_column(Integer, default=20)
status: Mapped[str] = mapped_column(String(30), default="draft", index=True)
notes: Mapped[str | None] = mapped_column(Text, nullable=True)
created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
