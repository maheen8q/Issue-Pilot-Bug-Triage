from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    analyze,
    dashboard,
    about,
    health,
    model_info,
)



app = FastAPI(
    title="IssuePilot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://issue-pilot-bug-triage.vercel.app",
    "https://issue-pilot-bug-triage-lnjojfgboj-maheens-projects-fbb3ff8f.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router)
app.include_router(dashboard.router)
app.include_router(about.router)
app.include_router(health.router)
app.include_router(model_info.router)

@app.get("/")
def root():
    return {
        "message": "IssuePilot API is running"
    }