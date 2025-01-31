from flask import Flask, request, jsonify
from models.bert_model import TaxQuestionAnswering
from models.gpt3_model import GPT3Answer

app = Flask(__name__)

tax_answer_model = TaxQuestionAnswering()
gpt3_answer_model = GPT3Answer(api_key="YOUR_API_KEY")

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question")
    context = data.get("context", "متن پیش‌فرض برای پردازش")

    answer = tax_answer_model.get_answer(question, context) if data.get("use_bert", False) else gpt3_answer_model.get_answer(question)
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
