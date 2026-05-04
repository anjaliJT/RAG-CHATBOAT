# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from app.core.config import settings

class VectorStoreManager:
    def __init__(self):
        # We will use OpenAI Embeddings by default for high quality RAG.
        # if not settings.OPENAI_API_KEY:
        #     raise ValueError("OPENAI_API_KEY is not set. Please set it in .env file.")
            
        self.embeddings = HuggingFaceEmbeddings(
                    model_name="all-MiniLM-L6-v2"
                )
        # self.embeddings = OpenAIEmbeddings(
        #     api_key=settings.OPENAI_API_KEY,s
        #     model="text-embedding-3-small"
        # )
        self.persist_directory = settings.CHROMA_PERSIST_DIR
        
        # Initialize the Chroma DB
        self.vector_store = Chroma(
            collection_name="enterprise_rag_collection",
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory
        )

    def add_documents(self, documents):
        """Add document chunks to the vector store."""
        self.vector_store.add_documents(documents)

    def get_retriever(self, k: int = 4):
        """Return a retriever with MMR search type for diverse results."""
        return self.vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": k, "fetch_k": k * 2}
        )

vector_store_manager = VectorStoreManager()
