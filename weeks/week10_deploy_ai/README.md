# week10_deploy_ai: deploy ai

## Concept
This week focuses on exposing AI pipelines as services. You will package logic behind an API, containerize it, and prepare a simple deployment path.

## Key Ideas
- Separate inference logic from transport layer (API).
- Validate request/response schemas.
- Keep deployment reproducible with Docker.
- Add health checks and basic observability from day one.

## Minimal Code Example
```python
"""Expose a small RAG endpoint with FastAPI.
Install: pip install fastapi uvicorn
Run: uvicorn app:app --reload
"""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from examples.rag_pipeline import generate_answer, retrieve


app = FastAPI(title="AI Engineer Demo API", version="0.1.0")


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
    chunks: list[str]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AnswerResponse)
def ask(payload: QuestionRequest) -> AnswerResponse:
    chunks = retrieve(payload.question, k=2)
    answer = generate_answer(payload.question, chunks)
    return AnswerResponse(answer=answer, chunks=chunks)
```

## Exercise
Create a Dockerfile for this API and run it locally on port `8000`.

## Extra Challenge
Deploy the container to a cloud service and add a `/metrics` endpoint for request counts and latency.
