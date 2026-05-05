# RAG-CHATBOT

## Overview
RAG-CHATBOT is a document-aware conversational AI system built using Retrieval-Augmented Generation (RAG). It enables users to ask questions and receive accurate, context-driven answers derived directly from provided documents.

The system works by retrieving relevant information from a custom knowledge base and using it to generate responses, reducing hallucinations and improving reliability compared to standard language models.

Designed to be flexible and extensible, the chatbot can be trained on any domain-specific dataset—such as company policies, technical documentation, or knowledge bases—making it suitable for a wide range of use cases including HR support, customer assistance, and internal knowledge management.

## Working Flow

1. **Document Ingestion**
   - Load HR PDFs
   - Clean and split into chunks

2. **Embedding Creation**
   - Convert text chunks → vectors
   - Store in vector database (FAISS/Chroma)

3. **Query Handling**
   - User query → embedding
   - Retrieve top-k relevant chunks

4. **Response Generation**
   - Pass context + query to LLM
   - Generate grounded answer

5. **(Optional) Agent Layer**
   - Decide retrieval strategy
   - Validate or refine responses


## Tech Stack

- Python  
- LangChain  
- FAISS / Chroma  
- OpenAI / Ollama  
- Streamlit / FastAPI  

## Goal

- Accurate HR Q&A chatbot  
- Minimal hallucination  
- Scalable + agent-ready architecture  

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd RAG-CHATBOAT
```

### 2. Install Dependencies
Make sure you have Python installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Backend (FastAPI)
Start the FastAPI server from the root directory:
```bash
uvicorn app.main:app --reload
```

### 4. Run the Frontend (Streamlit)
Open a new terminal, navigate to the `ui` directory, and start the Streamlit application:
```bash
cd ui
streamlit run app.py
```

### 5. Usage
- Open the Streamlit frontend in your browser (usually at `http://localhost:8501`).
- **Upload File:** Use the file uploader to upload your HR policy documents (PDFs).
- **Ask Question:** Type your query into the chat interface to get answers based on the uploaded documents.

### Screenshot
![Screenshot](<Screenshot 2026-05-04 at 4.45.33 PM.png>)
