from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mock_data import PAPERS
from models import Paper

app = FastAPI(title="Research Summarizer", description="Mock backend for Slackbot paper summarizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/papers", response_model=list[Paper])
def get_papers():
    return PAPERS
