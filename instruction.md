
1000# Industry-Grade Gen AI RAG Project

This is an enterprise-grade Retrieval-Augmented Generation (RAG) system built with FastAPI, LangChain, ChromaDB, and Streamlit. It allows you to upload documents (.pdf, .txt, .md), index them securely, and query them using OpenAI's state-of-the-art LLMs.

## Features
- **FastAPI Backend**: High-performance, async REST API for processing and querying.
- **Advanced RAG Pipeline**: Uses LangChain Expression Language (LCEL), OpenAI embeddings, and semantic chunking.
- **Local Vector Store**: ChromaDB used locally to persist and retrieve document embeddings.
- **Streamlit UI**: A clean, interactive web interface for uploading documents and chatting with your data.
- **Source Citations**: The AI responses include citations and the exact context chunks used.

---

## 🛠️ Prerequisites

1. **Python 3.9+**
2. **OpenAI API Key**: You need an API key from [OpenAI](https://platform.openai.com/).

---

## 🚀 Setup Instructions

### 1. Install Dependencies
Open your terminal and navigate to the project directory, then run:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
1. Copy the `.env.example` file and rename it to `.env`.
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your OpenAI API Key:
   ```env
   OPENAI_API_KEY=sk-your-real-api-key-here
   ```

---

## 🏃‍♂️ How to Run the Application

This project consists of two parts: the **FastAPI Backend** and the **Streamlit Frontend**. You need to run both simultaneously in separate terminal windows.

### Terminal 1: Start the Backend (FastAPI)
```bash
uvicorn app.main:app --reload
```
- The API will start at: `http://localhost:8000`
- You can access the automatic Swagger API documentation at: `http://localhost:8000/docs`

### Terminal 2: Start the Frontend (Streamlit UI)
```bash
streamlit run ui/app.py
```
- The Streamlit app will open in your browser automatically at: `http://localhost:8501`

---

## 🧪 Steps to Test and See Output

### Method 1: Using the Streamlit UI (Recommended)

1. Open your browser to `http://localhost:8501`.
2. **Upload a Document**:
   - Look at the left sidebar under "1. Document Management".
   - Click "Browse files" and select a `.pdf`, `.txt`, or `.md` file.
   - Click the **"Upload & Index"** button.
   - You should see a success message indicating the number of chunks indexed.
3. **Ask Questions**:
   - In the main chat area ("2. Ask Questions"), type a question related to the document you just uploaded.
   - The AI will process the query, retrieve relevant information, and generate an answer.
   - Click on the **"View Sources"** expander below the answer to see the exact text chunks the AI used to form its response.

### Method 2: Using the FastAPI Swagger UI (For Developers)

1. Open your browser to `http://localhost:8000/docs`.
2. **Upload a Document (`POST /api/v1/upload`)**:
   - Click on the `/api/v1/upload` endpoint to expand it.
   - Click **"Try it out"**.
   - Select a file using the file picker.
   - Click **"Execute"**. 
   - Scroll down to see the Server Response (it should return `status: "success"` and `chunks_indexed: N`).
3. **Query the Document (`POST /api/v1/query`)**:
   - Click on the `/api/v1/query` endpoint to expand it.
   - Click **"Try it out"**.
   - Edit the Request body to ask a question, for example:
     ```json
     {
       "query": "What is the main topic of the document?"
     }
     ```
   - Click **"Execute"**.
   - Look at the Server Response. You will see the `"answer"` string and the `"sources"` array containing the document snippets.

---

## 📁 Project Structure

```text
chat_model/
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Project dependencies
├── README.md             # This guide
├── app/                  # FastAPI Backend Source Code
│   ├── main.py           # API entrypoint
│   ├── core/
│   │   └── config.py     # Application settings
│   ├── api/
│   │   └── routes.py     # API Endpoints (Upload, Query)
│   ├── models/
│   │   └── schemas.py    # Pydantic schemas for data validation
│   ├── services/
│   │   ├── rag_service.py         # Core LangChain generation logic
│   │   └── document_processor.py  # File loading and chunking
│   └── vectorstore/
│       └── chroma_store.py        # ChromaDB setup and embedding logic
├── ui/
│   └── app.py            # Streamlit Chat Interface
└── data/                 # Auto-generated directory for stored data
    ├── chroma/           # Vector Database persistence folder
    └── uploads/          # Temporary file uploads folder
```
