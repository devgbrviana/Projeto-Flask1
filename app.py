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