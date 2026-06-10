from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# BASE_DIR = Path(__file__).resolve().parent.parent

# pdf_path = BASE_DIR / "DocumentLoader" / "Files" / "GRU.pdf"

def document_loader(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    return docs