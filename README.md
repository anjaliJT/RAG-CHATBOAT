# RAG-CHATBOAT

## Overview
RAG-CHATBOAT is an HR policy chatbot built using Retrieval-Augmented Generation (RAG). It answers user queries based on internal company documents with high accuracy and minimal hallucination.


## Project Structure
RAG-CHATBOAT/
│
├── app/
│ ├── main.py # Entry point (API / Streamlit app)
│ ├── config.py # Configurations (API keys, paths)
│
├── data/
│ ├── raw/ # Raw HR PDFs
│ ├── processed/ # Cleaned text files
│
├── ingestion/
│ ├── loader.py # Load PDFs
│ ├── splitter.py # Chunking logic
│ ├── embeddings.py # Generate embeddings
│
├── vectorstore/
│ ├── db.py # FAISS/Chroma setup
│
├── retriever/
│ ├── retriever.py # Query → relevant chunks
│
├── llm/
│ ├── generator.py # LLM response generation
│ ├── prompt.py # Prompt templates
│
├── agent/ (optional)
│ ├── agent.py # Decision-making logic
│
├── ui/
│ ├── streamlit_app.py # Chat interface
│
├── utils/
│ ├── logger.py
│ ├── helpers.py
│
├── requirements.txt
└── README.md



---

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
