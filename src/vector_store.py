from langchain_chroma import Chroma
DB_PATH = "chroma_db"

def create_vector_db(chunks, embedding_model):
    return Chroma.from_documents(
        documents=chunks,
        embedding= embedding_model,
        persist_directory=DB_PATH
    )
    
def load_vector_db(embedding_model):
    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model
    )
    
    