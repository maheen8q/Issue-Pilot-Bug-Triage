import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

PRIORITY_MODEL_PATH = BASE_DIR / "ML" / "artifacts" / "priority_model.pkl"
COMPONENT_MODEL_PATH = BASE_DIR / "ML" / "artifacts" / "component_model.pkl"


# Load models once when this module is imported
priority_model = joblib.load(PRIORITY_MODEL_PATH)
component_model = joblib.load(COMPONENT_MODEL_PATH)


def build_issue_text(title: str, description: str) -> str:
    """
    Combine title and description into a single text string
    for the ML models.
    """
    title = title.strip() if title else ""
    description = description.strip() if description else ""
    return f"{title} {description}".strip()


def predict_issue(title: str, description: str) -> dict:
    """
    Predict priority and component for a given issue.
    """
    issue_text = build_issue_text(title, description)

    priority = priority_model.predict([issue_text])[0]
    component = component_model.predict([issue_text])[0]

    return {
        "priority": priority,
        "component": component
    }