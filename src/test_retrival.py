from retrival import get_retreval
from embedding import embedding_model
embedding_model = embedding_model()

retriever = get_retreval(embedding_model)

docs = retriever.invoke(
    "What is GRU?"
)

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)
    print("=" * 50)