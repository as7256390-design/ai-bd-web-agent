AI BD Web Agent

Automated Lead Identification & Propensity Scoring for 3D In-Vitro Models

An AI-driven web agent that identifies, enriches, and prioritizes high-intent scientific and industry professionals relevant to 3D in-vitro models for therapy development. The system aggregates public scientific signals, enriches profiles with contextual intelligence, applies a weighted propensity-to-buy scoring model, and publishes ranked leads via an interactive dashboard and exportable outputs.

🔗 Live Demo

Streamlit App:
https://ai-bd-web-agent-qfekcjbp2qft2njtvatohm.streamlit.app/

📄 Sample Output

Ranked Leads (CSV):
https://raw.githubusercontent.com/as7256390-design/ai-bd-web-agent/main/data/output/sample_ranked_leads.csv

🎯 Problem Statement

Business development teams in biotech and life sciences face a recurring challenge:

Thousands of potential contacts exist, but few have real intent

Manual filtering of scientists, toxicologists, and safety leaders is slow

Funding readiness, scientific activity, and role relevance are rarely evaluated together

Traditional lead lists lack signal quality and prioritization logic.

💡 Solution Overview

This project implements an automated lead intelligence pipeline that:

Identifies relevant profiles using public scientific signals

Enriches each profile with contextual and inferred data

Scores leads using a transparent, weighted probability model

Publishes results in a format usable by BD and GTM teams

The focus is on verifiable, reproducible outputs, not static screenshots or videos.

🧱 High-Level Architecture

The system follows a modular, pipeline-oriented design executed on demand via the Streamlit UI.

Identify → Enrich → Score → Rank → Publish

Core Orchestration (app.py)
profiles = identify_profiles()
enriched = enrich_profiles(profiles)
ranked = score_profiles(enriched)


Each stage is isolated, testable, and extensible.

🔍 Pipeline Stages
1️⃣ Identification (Signal Ingestion)

Goal: Discover scientifically relevant professionals.

Sources

PubMed (recent publications related to liver toxicity, 3D models, NAMs)

Conference-style datasets (simulated but structured for extension)

Signals Captured

Author / researcher identity

Recency of scientific activity

Domain relevance (toxicology, safety, hepatic models)

2️⃣ Enrichment (Contextual Intelligence)

Goal: Convert raw names into actionable profiles.

Enrichment Includes

Role and seniority context

Person location vs. company HQ separation

Inferred business email patterns

Organizational readiness indicators (e.g., funding stage proxy)

Enrichment is intentionally conservative and transparent—no black-box scraping.

3️⃣ Ranking (Propensity-to-Buy Engine)

Goal: Prioritize leads by likelihood of engagement.

Each profile receives a 0–100 score based on weighted signals:

Signal Category	Example	Weight
Role Fit	Director of Toxicology, Safety Lead	+30
Scientific Intent	Recent publication in DILI / 3D models	+40
Funding Readiness	Series A/B or Grant-funded	+20
Technographic Fit	Uses in-vitro models, open to NAMs	+25
Location	Boston, Cambridge, Basel, Bay Area	+10

Final output is a rank-ordered lead list, not a flat dataset.

📊 Output & Consumption
Interactive Dashboard

Searchable table

One-click CSV export

Human-readable prioritization

Export Formats

CSV (Excel / Google Sheets ready)

Streamlit UI for real-time review

Designed for BD, partnerships, and research teams.

🧠 Key Design Decisions
✔ No LinkedIn Scraping

To respect platform ToS and avoid brittle workflows, the system relies on:

Public scientific data

Career signal proxies

Role and publication-based intent

✔ Explainable Scoring

Every score is traceable to explicit rules—no opaque ML model.

✔ Modular Extensibility

Each stage can be swapped or extended:

LinkedIn / Sales Navigator APIs

Crunchbase / PitchBook funding data

CRM integrations

🛠️ Tech Stack

Python 3

Streamlit – interactive UI

Pandas – data handling

Requests + BeautifulSoup – public data extraction

CSV / GitHub RAW – verifiable output delivery

⚙️ Local Setup
git clone https://github.com/as7256390-design/ai-bd-web-agent
cd ai-bd-web-agent
pip install -r requirements.txt
streamlit run app.py

🚀 Deployment

The live demo is deployed on Streamlit Cloud, ensuring:

Zero local setup for reviewers

Reproducible execution

Public verification of functionality

📈 Future Extensions

Direct LinkedIn API integration (via Proxycurl)

Funding intelligence via Crunchbase

Automated Google Sheets publishing

CRM-ready exports (HubSpot / Salesforce)

👤 Author

Ashutosh Sharma
AI & Data Science Undergraduate
Focus: AI systems, lead intelligence, and applied research
