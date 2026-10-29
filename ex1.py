from flask import Flask, jsonify, request

app = Flask(__name__)
id = 0
filmes_db = []

@app.route("/filmes", methods=["GET"])
def retornarFilmes():
    return jsonify(filmes_db)

@app.route("/filmes", methods=["POST"])
def salvarFilmes():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")
    filme = {"id": id, "nome": nome, "ano": ano, "diretor": diretor}
    filmes_db.append(filme)
    return jsonify(filme)

@app.route("/filmes/<int:id>", methods=["PUT"])
def editarFilmes(id):
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")
    for filme in filmes_db:
        if filme["id"] == id:
            filme["nome"] = nome
            filme["diretor"] = diretor
            filme["ano"] = ano
            return jsonify(filme), 200

    return jsonify({"erro": "Filme não encontrado"}), 404


@app.route("/filmes/<int:id>", methods=["DELETE"])
def removerFilmes(id):
    for filme in filmes_db:
        if filme["id"] == id:
            filmes_db.remove(filme)
        return "", 204

    return jsonify({"erro": "Filme não encontrado"}), 404


app.run(debug=True)
