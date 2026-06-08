from pdf_loader import document_loader
from file_chunking import chunking_document
from embedding import embedding_model
from vector_store import create_vector_db

# Documents loading 
docs = document_loader()

# creating chunks 
chunks = chunking_document(docs)

# Embedding model loading
embedding_model = embedding_model()

# create vector store
create_vector_db(
    chunks=chunks,
    embedding_model=embedding_model
)

print("Vector DB created sucessfuly")