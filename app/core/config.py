import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Enterprise Gen AI RAG API"
    API_V1_STR: str = "/api/v1"
    CHROMA_PERSIST_DIR :str = os.getenv("CHROMA_PERSIST_DIR")
    UPLOAD_DIR :str = os.getenv("UPLOAD_DIR")
    # OPENAI_API_KEY :str = os.getenv("OPENAI_API_KEY")
    HUGGINGFACEHUB_API_TOKEN :str = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    
    
    # RAG Settings
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    RETRIEVER_K: int = 4
    
    # Ensure directories exist
    def create_dirs(self):
        os.makedirs(self.CHROMA_PERSIST_DIR, exist_ok=True)
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
settings.create_dirs()
