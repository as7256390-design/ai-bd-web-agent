import pandas as pd

def enrich_profiles(df):
    """
    Enriches identified profiles with inferred contact and location data.
    """

    def infer_email(name, company):
        try:
            domain = company.replace(" ", "").lower()
            parts = name.split()
            first = parts[0].lower()
            last = parts[-1].lower()
            return f"{first}.{last}@{domain}.com"
        except:
            return "not_available@company.com"

    df["Email"] = df.apply(
        lambda row: infer_email(row["Name"], row["Company"]), axis=1
    )

    return df
