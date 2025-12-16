def score_profiles(df):
    """
    Computes a weighted propensity-to-buy score (0–100)
    for business development prioritization.
    """

    scores = []

    for _, row in df.iterrows():
        score = 0

        # Role fit
        if any(k in row["Title"] for k in ["Toxicology", "Safety", "Hepatic", "3D", "Director"]):
            score += 30

        # Funding / budget readiness
        if row["Funding Stage"] in ["Series A", "Series B", "Grant Funded"]:
            score += 20

        # Technographic readiness
        if row["Uses InVitro"] == "Yes":
            score += 15
        if row["Open to NAMs"] == "Yes":
            score += 10

        # Geographic innovation hubs
        if row["Company HQ"] in ["Boston", "Cambridge", "Basel", "Bay Area", "UK"]:
            score += 10

        # Scientific intent
        if row["Recent Publication"] == "Yes":
            score += 40

        scores.append(score)

    df["Probability Score"] = scores
    df = df.sort_values("Probability Score", ascending=False)
    df["Rank"] = range(1, len(df) + 1)

    return df
