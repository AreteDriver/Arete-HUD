from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import context_manager
import agents

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    providers: list[str]
    topics: list[str] = []

class AskResponse(BaseModel):
    responses: dict

@app.get("/topics")
def get_topics():
    return context_manager.get_topics()

@app.get("/context")
def get_context():
    return context_manager.get_context()

@app.post("/ask")
def ask_multi_ai(req: AskRequest):
    responses = {}
    for provider in req.providers:
        responses[provider] = agents.ask_agent(provider, req.question, req.topics)
    return {"responses": responses}

@app.post("/analyze")
def analyze_diff(data: dict):
    return agents.analyze_differences(data)

@app.post("/synthesize")
def synthesize_master(data: dict):
    return agents.synthesize_answer(data)
