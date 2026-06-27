import joblib
import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parents[2]

SIMILARITY_VECTORIZER_PATH = BASE_DIR / "ML" / "artifacts" / "similarity_vectorizer.pkl"
ISSUE_VECTORS_PATH = BASE_DIR / "ML" / "artifacts" / "issue_vectors.pkl"
ISSUES_CSV_PATH = BASE_DIR / "ML" / "data" / "issues_for_similarity.csv"


# Load similarity assets once
similarity_vectorizer = joblib.load(SIMILARITY_VECTORIZER_PATH)
issue_vectors = joblib.load(ISSUE_VECTORS_PATH)
issues_df = pd.read_csv(ISSUES_CSV_PATH)


def build_issue_text(title: str, description: str) -> str:
    """
    Combine title and description into a single text string
    for similarity search.
    """
    title = title.strip() if title else ""
    description = description.strip() if description else ""
    return f"{title} {description}".strip()


def find_similar_issues(title: str, description: str, top_k: int = 3) -> list:
    """
    Return top_k similar historical issues.
    """
    issue_text = build_issue_text(title, description)
    # Vectorize the incoming issue text
    query_vector = similarity_vectorizer.transform([issue_text])
    # Compute cosine similarity against all historical issue vectors
    similarities = cosine_similarity(query_vector, issue_vectors).flatten()
    # Get top matching indices
    top_indices = similarities.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        row = issues_df.iloc[idx]

        issue_url = str(row.get("issue_url", "")).strip().strip('"')
        title = str(row.get("title", "")).strip().strip('"')

        results.append({
            "issue_url": issue_url,
            "title": title,
            "similarity_score": round(float(similarities[idx]), 4)
        })

    return results