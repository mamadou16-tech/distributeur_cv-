"""Modèle Application : candidature générée, envoyée et suivie."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Application(Base):
    """Une candidature : entreprise + CV sélectionné + email généré.

Statuts : to_review, pending_validation, sent, response_received,
    interview, rejected, no_response, follow_up_due.
    """

__tablename__ = "applications"

id: Mapped[int] = mapped_column(primary_key=True)
campaign_id: Mapped[int | None] = mapped_column(
    ForeignKey("campaigns.id", ondelete="SET NULL"), nullable=True
)
company_id: Mapped[int] = mapped_column(
    ForeignKey("companies.id", ondelete="CASCADE"), index=True
)
opportunity_id: Mapped[int | None] = mapped_column(
    ForeignKey("opportunities.id", ondelete="SET NULL"), nullable=True
)
resume_id: Mapped[int] = mapped_column(
    ForeignKey("resumes.id", ondelete="RESTRICT"), index=True
)
match_score: Mapped[float | None] = mapped_column(Float, nullable=True)
match_explanation: Mapped[str | None] = mapped_column(Text, nullable=True)
email_subject: Mapped[str | None] = mapped_column(String(255), nullable=True)
email_body: Mapped[str | None] = mapped_column(Text, nullable=True)
status: Mapped[str] = mapped_column(String(30), default="to_review", index=True)
sent_at: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True), nullable=True
)
response_received_at: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True), nullable=True
)
created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now()
)
updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
)
