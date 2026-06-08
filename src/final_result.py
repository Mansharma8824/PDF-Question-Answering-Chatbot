from qa_result import create_qa_rag

question = "Expalin about GRU in deep learning."

final_res = create_qa_rag(question)

print(final_res.content)