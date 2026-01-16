# Agentic AI Multi-Tool System

An Agentic AI system built using LangChain-style multi-agent orchestration and Retrieval-Augmented Generation (RAG).  
The system autonomously plans, retrieves context, reasons, and executes tasks using LLMs and external tools.

## Features
- Multi-agent architecture (Planner, Retriever, Executor, Verifier)
- Tool calling with RAG integration
- Semantic search using vector databases
- REST APIs with FastAPI
- Streamlit-based UI
- Dockerized deployment
- GCP + Vertex AI ready

## Tech Stack
- Python, LangChain
- HuggingFace Transformers
- FAISS / Chroma
- FastAPI, Streamlit
- Docker
- GCP (Vertex AI, Cloud Run)

## Run Locally
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
