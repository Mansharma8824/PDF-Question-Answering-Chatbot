from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the question using ONLY the provided context.

If the answer is not found in the context,
say "I could not find the answer in the document."

Context:
{context}

Question:
{question}
"""
)