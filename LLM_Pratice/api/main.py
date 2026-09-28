from fastapi import FastAPI
from pydantic import BaseModel

from llm.llm_client import ask_llm


app = FastAPI(
    title="Local LLM API",
    description="FastAPI wrapper for a local Ollama LLM",
    version="1.0.0"
)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {
        "message": "Local LLM API is running"
    }


@app.post("/ask")
def ask(request: PromptRequest):

    response = ask_llm(request.prompt)

    return {
        "prompt": request.prompt,
        "response": response
    }