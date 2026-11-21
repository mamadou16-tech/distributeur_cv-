"""Validation Phase 1 : connexion DB, tables, chaîne FK complète."""
import sys

sys.path.insert(0, ".")

from sqlalchemy import create_engine, select  # noqa: E402
from sqlalchemy.orm import Session  # noqa: E402

from app.config import settings  # noqa: E402
from app.models import (  # noqa: E402
    AgentRun, Application, Base, Campaign, Company, Opportunity, Resume,
)

engine = create_engine(settings.sqlalchemy_url, pool_pre_ping=True)
Base.metadata.create_all(engine)

expected = {"resumes", "companies", "opportunities", "campaigns", "applications", "agent_runs"}
missing = expected - set(Base.metadata.tables.keys())
assert not missing, f"Tables manquantes : {missing}"
print("[1/3] Tables OK :", ", ".join(sorted(Base.metadata.tables.keys())))

with Session(engine) as s:
    r = Resume(label="CV - IA & Data Science", original_filename="cv_ia.pdf", file_path="uploads/cv_ia.pdf")
    c = Company(name="Acme Robotics", country="France", sector="Industrie")
    s.add(r); s.add(c); s.flush()

o = Opportunity(company_id=c.id, title="Stage Data Science", contract_type="stage")
camp = Campaign(name="Stage IA 2027", send_mode="manual")
s.add(o); s.add(camp); s.flush()

a = Application(
        company_id=c.id, opportunity_id=o.id, resume_id=r.id, campaign_id=camp.id,
        match_score=87.5, status="to_review",
        email_subject="Candidature - Stage Data Science", email_body="Bonjour, ...",
    )
run = AgentRun(agent_name="resume_analyzer", status="success", trigger="upload",
                input_data={"resume_id": r.id}, output_data={"skills": ["python"]})
s.add(a); s.add(run); s.commit()

with Session(engine) as s:
    row = s.scalars(select(Application)).one()
    assert row.resume_id <mark> 1 and row.company_id <mark> 1
    comp = s.get(Company, row.company_id)
    assert len(comp.opportunities) == 1
    print(f"[2/3] Chaîne FK OK : Application -> Resume#{row.resume_id}, "
          f"Company#{row.company_id}, Opportunity#{row.opportunity_id}, "
          f"score={row.match_score}")

# Nettoyage des données de test pour garder une base propre
    for table in reversed(Base.metadata.sorted_tables):
        s.execute(table.delete())
    s.commit()

print("[3/3] Nettoyage OK — base prête.")
print("PHASE 1 VALIDÉE ✅")
