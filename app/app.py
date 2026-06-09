from flask import Flask, render_template, request,jsonify


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
    return jsonify({
        "answer": f"You asked: {question}"
    })



if __name__ == "__main__":
    app.run(debug=True)