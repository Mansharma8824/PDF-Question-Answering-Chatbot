
from .vector_store import load_vector_db

def get_retreval(embedding_model):
    vector_store = load_vector_db(
        embedding_model= embedding_model
    )
    
    retrival = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    
    return retrival

