from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def chat_LLM():
    llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.5-flash-lite',
         max_tokens=50
    )
    return llm 
