from fastapi import FastAPI
from workflows.langgraph_flow import run_workflow

app = FastAPI()

@app.post("/query")
def query_agent(payload: dict):
    return {"response": run_workflow(payload["query"])}
