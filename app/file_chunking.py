from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunking_document(docs):

    spliter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100
    )

    chunks = spliter.split_documents(docs)
    return chunks