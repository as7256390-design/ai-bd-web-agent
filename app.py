import streamlit as st
import pandas as pd
from crawler import identify_profiles
from enrichment import enrich_profiles
from scoring import score_profiles

st.set_page_config(page_title="AI BD Web Agent", layout="wide")

st.title("AI Web Agent – Lead Qualification Dashboard")

st.markdown(
    "This tool identifies, enriches, and ranks high-intent leads for 3D in-vitro model adoption."
)

if st.button("Run Lead Generation Engine"):
    profiles = identify_profiles()
    enriched = enrich_profiles(profiles)
    ranked = score_profiles(enriched)

    st.success("Lead generation and ranking completed.")

    st.dataframe(ranked, use_container_width=True)

    csv = ranked.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Ranked Leads (CSV)",
        csv,
        "ranked_leads.csv",
        "text/csv"
    )
