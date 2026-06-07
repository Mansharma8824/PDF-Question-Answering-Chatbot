from pdf_loader import document_loader
from file_chunking import chunking_document
from embedding import embedding_model

# Documents loading 
docs = document_loader()

# creating chunks 
chunks = chunking_document(docs)

# Embedding model loading
embedding_model = embedding_model()

vector = embedding_model.embed_query(
    chunks[0].page_content
)


print(f" Total file : {len(docs)},\n total chunks : {len(chunks)}")
print(f"length of page: {len(chunks)}")
print(f"length of embedded: {len(vector)}")