from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = "default"

class SourceDocument(BaseModel):
    page_content: str
    metadata: Dict[str, Any]

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]

class DocumentUploadResponse(BaseModel):
    filename: str
    status: str
    chunks_indexed: int
