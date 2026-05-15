from flask import Flask, jsonify, request
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

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de usuarios - Acesse /usuarios"})


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)


@app.route("/usuarios", methods=["POST"])
def criar_usuario():

    novo = request.json

    novo['id'] = len(usuarios) + 1

    usuarios.append(novo)

    return jsonify(novo), 201



@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):

    for usuario in usuarios:

        if usuario["id"] == id:

            dados = request.json

            usuario["nome"] = dados["nome"]

            return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):

    for usuario in usuarios:

        if usuario["id"] == id:

            usuarios.remove(usuario)

            return jsonify({"mensagem": "Usuário deletado com sucesso"})

    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
