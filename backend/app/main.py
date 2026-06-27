from fastapi import FastAPI
from app.schemas import AnalyzeRequest, AnalyzeResponse, SimilarIssue
from app.services.predictor import predict_issue
from app.services.similarity import find_similar_issues
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="IssuePilot",
    description="ML-powered bug triage service for predicting priority, component, and retrieving similar issues.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "IssuePilot API is running"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_issue(request: AnalyzeRequest):
    # Get predictions
    prediction = predict_issue(request.title, request.description)

    # Get similar issues
    similar_issues_raw = find_similar_issues(request.title, request.description, top_k=3)

    # Convert raw dicts into SimilarIssue schema objects
    similar_issues = [SimilarIssue(**issue) for issue in similar_issues_raw]

    return AnalyzeResponse(
        priority=prediction["priority"],
        component=prediction["component"],
        similar_issues=similar_issues
    )