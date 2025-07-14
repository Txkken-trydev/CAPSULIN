from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch
import sqlite3
import random

app = Flask(__name__)

# Configurar ChatterBot
chatbot = ChatBot(
    "Capsulin",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.LevenshteinDistance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ],
    read_only=True
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish.greetings")

# Funcion para consultar DB
def consultar_db(query, params=(), fetch='all'):
    conn = sqlite3.connect("medicamentos.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    if fetch == 'one':
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    conn.close()
    return result

def obtener_sintomas():
    rows = consultar_db("SELECT sintomas FROM medicamentos")
    sintomas = set()
    for row in rows:
        for sintoma in row[0].split(","):
            sintomas.add(sintoma.strip().lower())
    return list(sintomas)

def obtener_componentes():
    rows = consultar_db("SELECT componentes FROM medicamentos")
    componentes = set()
    for row in rows:
        for componente in row[0].split(","):
            componentes.add(componente.strip().lower())
    return list(componentes)

def consultar_por_sintoma(sintoma):
    return consultar_db("SELECT nombre, uso FROM medicamentos WHERE sintomas LIKE ?", (f"%{sintoma}%",))

def consultar_por_categoria(categoria):
    return consultar_db("SELECT nombre, uso, categoria FROM medicamentos WHERE sintomas LIKE ?", (f"%{categoria}%",))

def consultar_por_componente(componente):
    return consultar_db("SELECT nombre, uso FROM medicamentos WHERE componentes LIKE ?", (f"%{componente}%",))

def consultar_por_nombre(nombre):
    return consultar_db("SELECT nombre, uso, presentacion FROM medicamentos WHERE LOWER(nombre) LIKE ?", (f"%{nombre.lower()}%",))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    palabras = user_input.split()
    respuesta = None

    # Buscar por síntomas dinámicamente
    sintomas = obtener_sintomas()
    for sintoma in sintomas:
        if sintoma in user_input:
            resultados = consultar_por_sintoma(sintoma)
            if resultados:
                recomendado = random.choice(resultados)
                respuesta = f"Te recomiendo: {recomendado[0]} (uso: {recomendado[1]}) para {sintoma}."
            else:
                respuesta = f"No encontré medicamentos para el síntoma: {sintoma}."
            break

    # Buscar por componentes dinámicamente
    if not respuesta:
        componentes = obtener_componentes()
        for componente in componentes:
            if componente in user_input:
                resultados = consultar_por_componente(componente)
                if resultados:
                    recomendado = random.choice(resultados)
                    respuesta = f"Te recomiendo: {recomendado[0]} (uso: {recomendado[1]})."
                else:
                    respuesta = f"No encontré medicamentos con el componente: {componente}."
                break

    # Preguntas generales y por nombre de medicamento
    if not respuesta:
        preguntas_generales = [
            "para que sirve",
            "que es",
            "como se usa",
            "como uso",
            "uso",
            "presentacion"
            "categoria",
        ]
        if any(pregunta in user_input for pregunta in preguntas_generales):
            nombres_db = set([row[0] for row in consultar_por_nombre("")])
            for nombre in nombres_db:
                if nombre in user_input:
                    resultados = consultar_por_nombre(nombre)
                    if resultados:
                        recomendado = random.choice(resultados)
                        respuesta = (
                            f"{recomendado[0]} se usa como: {recomendado[1]}. "
                            f"Presentación: {recomendado[2]}"
                        )
                    else:
                        respuesta = f"No encontré información sobre: {nombre}."
                    break
            if not respuesta:
                respuesta = "¿Sobre qué medicamento deseas información?"
        else:
            respuesta = str(chatbot.get_response(user_input))

    return jsonify({"response": respuesta})

if __name__ == "__main__":
    app.run(debug=True)