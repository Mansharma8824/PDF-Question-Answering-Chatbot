from flask import Flask, render_template, request, jsonify
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.qa_result import create_qa_rag


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



if __name__ == "__main__":
    app.run(debug=True)