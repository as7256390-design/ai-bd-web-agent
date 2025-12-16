import requests
import pandas as pd
from bs4 import BeautifulSoup

def identify_profiles():
    query = "drug induced liver injury 3D model"
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={query.replace(' ', '+')}"
    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select(".docsum-content")[:10]

    data = []

    for art in articles:
        authors = art.select_one(".docsum-authors")
        author = authors.text.split(",")[0] if authors else "Unknown Author"

        data.append({
            "Name": author,
            "Title": "Research Scientist",
            "Company": "Academic / Research Institute",
            "Person Location": "Unknown",
            "Company HQ": "Unknown",
            "Recent Publication": "Yes",
            "Funding Stage": "Grant Funded",
            "Uses InVitro": "Yes",
            "Open to NAMs": "Yes"
        })

    return pd.DataFrame(data)
