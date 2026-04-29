import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.models.schemas import QueryRequest, QueryResponse, DocumentUploadResponse, SourceDocument
from app.services.document_processor import document_processor
from app.vectorstore.chroma_store import vector_store_manager
from app.services.rag_service import rag_service
from app.core.config import settings

router = APIRouter()

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document (PDF, TXT, MD), process it into chunks, and index it in the vector store.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
        
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in [".pdf", ".txt", ".md"]:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file format: {file_extension}. Only .pdf, .txt, and .md are supported."
        )

    file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
    
    try:
        # Save uploaded file to disk
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Process document
        chunks = document_processor.load_and_split(file_path)
        
        if not chunks:
            raise HTTPException(status_code=400, detail="No text could be extracted from the document.")
            
        # Add source metadata to chunks
        for chunk in chunks:
            chunk.metadata["source"] = file.filename
            
        # Index in Vector Store
        vector_store_manager.add_documents(chunks)
        
        return DocumentUploadResponse(
            filename=file.filename,
            status="success",
            chunks_indexed=len(chunks)
        )
        
    except Exception as e:
        # Clean up file if processing fails
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Query the RAG system based on the uploaded documents.
    """
    try:
        answer, docs = rag_service.query(request.query)
        
        # Format sources
        sources = [
            SourceDocument(
                page_content=doc.page_content,
                metadata=doc.metadata
            )
            for doc in docs
        ]
        
        return QueryResponse(
            answer=answer,
            sources=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
