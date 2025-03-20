from flask import Flask, request, jsonify

app = Flask(__name__)

professores = []
alunos = []
turmas = []


@app.route('/reseta', methods=['POST'])
def reseta():
    alunos.clear()
    professores.clear()
    turmas.clear()
    return jsonify({'status': 'dados resetados'}), 200


@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(professores)


@app.route('/professores', methods=['POST'])
def criar_professor():
    try:
        data = request.get_json()
        novo_professor = {
            "id": len(professores) + 1,
            "nome": data["nome"],
            "especialidade": data["especialidade"],
            "idade": data["idade"],
            "info": data["info"]
        }
        professores.append(novo_professor)
        return jsonify(novo_professor)
    except Exception:
        return jsonify({"erro": "Erro ao criar professor"})