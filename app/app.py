from flask import Flask, render_template, request, jsonify
import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.qa_result import create_qa_rag

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = BASE_DIR / "DocumentLoader" / "Files"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html"
    )

@app.route("/chat", methods = ['POST'])
def chat():
    data = request.get_json()
    
    question = data['question']

    final_res = create_qa_rag(question)

    print(final_res.content)
    return jsonify({
        "answer": f"{final_res.content}"
    })
    
    
    
@app.route("/upload", methods = ['POST'])
def upload():
    file = request.files.get("pdf")
    
    if not file:
        return jsonify({
            "message": "No file selected"
        }), 400
    
    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    return jsonify({
        "message": "PDF uploaded successfully",
        "filename": file.filename
    })



if __name__ == "__main__":
    app.run(debug=True)