# 📄 PDF Question Answering Chatbot

An AI-powered chatbot that allows users to upload PDF documents and ask questions based on the content of those documents.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from PDFs and generate accurate responses using Large Language Models (LLMs).

---

## 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into chunks
- Generate embeddings
- Store embeddings in ChromaDB
- Semantic search for relevant chunks
- Question answering using Gemini/OpenAI
- Chat interface using Flask
- Real-time response generation

---

## 🏗️ Project Architecture

```text
User Question
      │
      ▼
Flask Application
      │
      ▼
Vector Database (ChromaDB)
      │
Retrieve Relevant Chunks
      │
      ▼
Gemini/OpenAI LLM
      │
      ▼
Generated Answer
```

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI/LLM
- LangChain
- Google Gemini API
- OpenAI API

### Vector Database
- ChromaDB

### Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter

### Embeddings
- HuggingFaceEmbeddings

---

## 📂 Project Structure

```text
PDF-Question-Answering-Chatbot/
├───app
│   │   app.py
│   │   
│   ├───static
│   │   ├───css
│   │   │       style.css
│   │   │       
│   │   └───js
│   │           script.js
│   │           
│   └───templates
│           index.html
│           
├───chroma_db   -> will be created by me
│           
├───DocumentLoader
│   └───Files
│           uploaded_file.pdf  -> file will upload by UI
│           
└───src
│    │   chatmodel.py
│    │   create_prompt.py
│    │   embedding.py
│    │   file_chunking.py
│    │   final_result.py
│    │   ingestion.py
│    │   pdf_loader.py
│    │   qa_result.py
│    │   retrival.py
│    │   vector_store.py
│    │
│
├───.env
├───requirements.txt
├───README.md
├───.gitignore

```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Mansharma8824/PDF-Question-Answering-Chatbot.git
```

### Navigate to Project

```bash
cd PDF-Question-Answering-Chatbot
```

### Create Virtual Environment

```bash
UV venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run Application

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000
```

---

## 🔄 Workflow

1. User uploads PDF
2. PDF text is extracted
3. Text is split into chunks
4. Embeddings are generated
5. Embeddings are stored in ChromaDB
6. User asks a question
7. Relevant chunks are retrieved
8. LLM generates an answer
9. Response is displayed in chat

---

## 📸 Screenshots

Add screenshots here after completing the UI.

### Home Page

![Home Page](screenshots/home.png)

### Chat Interface

![Chat](screenshots/chat.png)

---

## 🎯 Future Improvements

- Multiple PDF support
- Chat history
- User authentication
- Streaming responses
- Source citations
- Docker deployment
- Cloud deployment (AWS/Azure/GCP)

---

## 👨‍💻 Author

Manish Kumar
LinkedIn: https://www.linkedin.com/in/manish-kumar-2518b6242/
