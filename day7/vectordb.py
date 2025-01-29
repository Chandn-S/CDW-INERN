from langchain_chroma import Chroma # type: ignore
import models # type: ignore
import utils

def initialize_chroma(persist_directory="./chroma_db"):
    """
    Initializes and returns a Chroma vector store.

    Args:
        persist_directory (str): Directory to store ChromaDB.
    
    Returns:
        Chroma: Initialized Chroma vector store.
    """
    hf_embeddings = models.create_hugging_face_embedding_model()
    vectorstore = Chroma(embedding_function=hf_embeddings, persist_directory=persist_directory)
    return vectorstore

#### INDEXING ####
def store_pdf_in_chroma(uploaded_file, vectorstore):
    """
    Processes a PDF file and stores its embeddings in ChromaDB.

    Args:
        uploaded_file: File for RAG ingestion pipeline.
        vectorstore: Instance of Chroma vector store.        
    """
    splits = utils.process_pdf_for_rag(uploaded_file)
    vectorstore.add_documents(splits)

#### RETRIEVAL ####
def retrieve_from_chroma(query, vectorstore):
    """
    Retrieves relevant documents from Chroma based on a query.

    Args:
        query (str): The query string for searching the vector store.
        vectorstore: The Chroma vector store instance.

    Returns:
        list: Relevant documents retrieved from Chroma.
    """
    retriever = vectorstore.as_retriever()
    documents = retriever.get_relevant_documents(query)
    return documents
