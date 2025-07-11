from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sqlite3

app = Flask(__name__)

# Configura ChatterBot
chatbot = ChatBot("Capsulin", read_only=True)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

# Función para consultar SQLite
def consultar_por_componente(componente):
    conn = sqlite3.connect("medicamentos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM medicamentos WHERE componentes LIKE ?", ('%' + componente + '%',))
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
        posible_componente = palabras[-1]
        resultados = consultar_por_componente(posible_componente)

        if resultados:
            respuesta = f"Los medicamentos que contienen {posible_componente} son: {', '.join(resultados)}."
        else:
            respuesta = "No encontré medicamentos con ese componente."
    else:
        respuesta = str(chatbot.get_response(user_input))

    return jsonify({"response": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
