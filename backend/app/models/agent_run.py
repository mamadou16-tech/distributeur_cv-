"""Modèle AgentRun : trace d'exécution d'un agent IA."""
from datetime import datetime

from sqlalchemy import DateTime, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class AgentRun(Base):
    """Trace d'une exécution d'agent (auditabilité des décisions de l'IA).

Agents prévus : resume_analyzer, company_research, opportunity,
    matching, email_generation, application, follow_up.
    """

__tablename__ = "agent_runs"

id: Mapped[int] = mapped_column(primary_key=True)
agent_name: Mapped[str] = mapped_column(String(50), index=True)
status: Mapped[str] = mapped_column(String(20), default="running", index=True)
trigger: Mapped[str | None] = mapped_column(String(100), nullable=True)
input_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
output_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
started_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), server_default=func.now()
)
finished_at: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True), nullable=True
)
