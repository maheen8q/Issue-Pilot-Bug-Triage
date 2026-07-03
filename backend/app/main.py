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
        "https://issuepilot.me",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
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