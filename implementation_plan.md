# Industry-Grade RAG Project Implementation Plan

This document outlines the architecture, tooling, and implementation steps for building an industry-grade Retrieval-Augmented Generation (RAG) system. The project will be built in the `chat_model` directory.

## Goal
To build a scalable, well-documented, and modular Gen AI project demonstrating advanced RAG capabilities. The system will allow users to upload documents (PDF/TXT), index them into a vector database, and query them using an LLM.

## User Review Required

> [!IMPORTANT]
> **LLM Provider Decision**: This plan defaults to using **OpenAI** (requires an `OPENAI_API_KEY`). Are you comfortable using OpenAI, or would you prefer a fully local open-source setup (e.g., HuggingFace embeddings + Ollama/Llama.cpp)? 
> Using OpenAI is standard for "industry-grade" reliability, but local models are great for privacy/cost. Let me know your preference.

## Open Questions

1. **Frontend**: Do you want a simple UI (like Streamlit) to interact with the API, or is a robust FastAPI backend with Swagger UI sufficient for this showcase?
2. **Document Types**: The initial plan supports PDFs and text files. Are there other formats (like CSVs or Docx) you need to support immediately?

## Proposed Architecture

- **Web Framework**: FastAPI (High performance, async, built-in Swagger docs).
- **Orchestration**: LangChain (Industry standard for building LLM applications).
- **Vector Database**: ChromaDB (Local, easy to setup without external infra, but scalable).
- **Embeddings**: OpenAI Embeddings (`text-embedding-3-small`).
- **LLM**: ChatOpenAI (`gpt-4o-mini` or `gpt-3.5-turbo`).
- **Advanced RAG Features**:
  - Document chunking using `RecursiveCharacterTextSplitter` with optimal overlap.
  - MMR (Maximal Marginal Relevance) retrieval to ensure diverse results.
  - Conversational memory (optional, configurable via LCEL).
  - Custom system prompts to prevent hallucinations.

## Proposed Changes

### Project Structure Setup

We will create a structured, modular Python project layout.

#### [NEW] `requirements.txt`
Dependencies including `fastapi`, `uvicorn`, `langchain`, `langchain-openai`, `chromadb`, `pypdf`, `pydantic-settings`, `python-multipart`.

#### [NEW] `.env.example`
Template for environment variables (API keys, config parameters).

#### [NEW] `README.md`
Comprehensive guide on how to set up, run, and understand the RAG architecture and the code.

### Core Backend (FastAPI & LangChain)

#### [NEW] `app/main.py`
FastAPI entrypoint, CORS setup, and API router inclusion.

#### [NEW] `app/core/config.py`
Configuration management using Pydantic `BaseSettings`.

#### [NEW] `app/models/schemas.py`
Pydantic schemas for request validation (e.g., `QueryRequest`, `QueryResponse`, `DocumentUploadResponse`).

#### [NEW] `app/api/routes.py`
API endpoints:
- `POST /upload`: Endpoint to upload and index documents.
- `POST /query`: Endpoint to ask questions against the uploaded documents.

#### [NEW] `app/services/document_processor.py`
Logic for loading documents (`PyPDFLoader`, `TextLoader`) and chunking them securely.

#### [NEW] `app/vectorstore/chroma_store.py`
Wrapper class to initialize ChromaDB, generate embeddings, and store/retrieve chunks.

#### [NEW] `app/services/rag_service.py`
The core LangChain logic. Combines the retriever, the LLM, and the prompt template using LangChain Expression Language (LCEL) to generate the final answer based on retrieved context.

## Verification Plan

### Automated/Local Testing
- Start the FastAPI server (`uvicorn app.main:app --reload`).
- Ensure Swagger UI is accessible at `http://localhost:8000/docs`.

### Manual Verification
- **Upload Flow**: Use Swagger to upload a sample PDF. Verify the response indicates successful chunking and indexing.
- **Query Flow**: Use Swagger to send a query related to the uploaded document. Verify the LLM response is accurate and cites the relevant context.
