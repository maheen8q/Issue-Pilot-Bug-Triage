from pydantic import BaseModel
from typing import List


class AnalyzeRequest(BaseModel):
    title: str
    description: str


class SimilarIssue(BaseModel):
    issue_url: str
    title: str
    similarity_score: float


class AnalyzeResponse(BaseModel):
    priority: str
    component: str
    similar_issues: List[SimilarIssue]