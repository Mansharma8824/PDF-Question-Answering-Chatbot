from .retrival import get_retreval
from .embedding import embedding_model as get_embedding_model
from .create_prompt import RAG_PROMPT
from .chatmodel import chat_LLM

embedding_model = get_embedding_model()

def create_qa_rag(question):
    retriever = get_retreval(embedding_model)

    docs = retriever.invoke(question)
    
    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    
    prompt = RAG_PROMPT.format(
        context = context,
        question = question
    )
    
    llm = chat_LLM()
    
    response = llm.invoke(prompt)
    
    return response


