from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch
import sqlite3

app = Flask(__name__)

# Configurar ChatterBot
chatbot = ChatBot("Capsulin", read_only=True)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")
logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Lo siento, no entendí eso.",
            "maximum_similarity_threshold": 0.80
        }
    ]
# Función para consultar DB
def consultar_por_medicamento(medicamentos):
    conn = sqlite3.connect("medicamentos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM medicamentos WHERE componentes LIKE ?", ('%' + '%',))
    resultados = cursor.fetchall()
    conn.close()
    return [r[0] for r in resultados]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if "contienen" in user_input or "componentes" in user_input:
        palabras = user_input.split()
        posible_medicamento = palabras[-1]
        resultados = consultar_por_medicamento(posible_medicamento)

        if resultados:
            respuesta = f"Los medicamentos que contienen {posible_medicamento} son: {', '.join(resultados)}."
        else:
            respuesta = "No encontré medicamentos con ese componente."
    else:
        respuesta = str(chatbot.get_response(user_input))

    return jsonify({"response": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
