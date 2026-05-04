# from langchain_openai import ChatOpenAI
from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.vectorstore.chroma_store import vector_store_manager
from app.core.config import settings
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
class RAGService:
    def __init__(self):
        # Using a solid default model for RAG tasks
        self.llm = Ollama(model="llama3")
        # self.llm =  HuggingFaceHub(
        #     repo_id="mistralai/Mistral-7B-Instruct",
        #     huggingfacehub_api_token=settings.HUGGINGFACEHUB_API_TOKEN,
        #         )
        # self.llm = ChatOpenAI(
        #     api_key=settings.HUGGINGFACEHUB_API_TOKEN,
        #     model="gpt-4o-mini",
        #     temperature=0.0
        # )
        self.retriever = vector_store_manager.get_retriever(k=settings.RETRIEVER_K)
        
        # System prompt designed to prevent hallucination and enforce context usage
        system_template = """You are an expert AI assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer or the context doesn't contain the answer, just say that you don't know. 
Do not make up an answer. Keep the answer concise and professional.

Context: {context}

Question: {question}

Answer:"""
        self.prompt = ChatPromptTemplate.from_template(system_template)

        # Build the LCEL (LangChain Expression Language) chain
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.rag_chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def query(self, question: str):
        """Execute a query against the RAG pipeline."""
        # Get the retrieved documents to return them as sources
        retrieved_docs = self.retriever.invoke(question)
        
        # Generate the answer using the chain
        answer = self.rag_chain.invoke(question)
        
        return answer, retrieved_docs

rag_service = RAGService()
