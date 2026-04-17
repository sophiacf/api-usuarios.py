from flask import Flask, jsonify
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Bruno"},
    {"id": 3, "nome": "Carla"},
    {"id": 4, "nome": "Diego"},
    {"id": 5, "nome": "Eduarda"},
    {"id": 6, "nome": "Felipe"},
    {"id": 7, "nome": "Gabriela"},
    {"id": 8, "nome": "Henrique"},
    {"id": 9, "nome": "Isabela"},
    {"id": 10, "nome": "João"},
    {"id": 11, "nome": "Karina"},
    {"id": 12, "nome": "Lucas"},
    {"id": 13, "nome": "Mariana"},
    {"id": 14, "nome": "Nathan"},
    {"id": 15, "nome": "Olívia"},
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de usuarios - Acesse /usuarios"})

@app.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
