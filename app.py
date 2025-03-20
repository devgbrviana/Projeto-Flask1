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
    

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    try:
        for professor in professores:
            if professor["id"] == id:
                data = request.get_json()
                professor["nome"] = data.get("nome", professor["nome"])
                professor["especialidade"] = data.get("especialidade", professor["especialidade"])
                professor["idade"] = data.get("idade", professor["idade"])
                professor["info"] = data.get("info", professor["info"])
                return jsonify(professor)
        return jsonify({"erro": "Professor não encontrado"}), 404
    except Exception:
        return jsonify({"erro": "Erro ao atualizar professor"}), 500


@app.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    try:
        for professor in professores:
            if professor["id"] == id:
                professores.remove(professor)
                return jsonify({"mensagem": "Professor deletado"})
        return jsonify({"erro": "Professor não encontrado"}), 404
    except Exception:
        return jsonify({"erro": "Erro ao deletar professor"}), 500

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    try:
        data = request.get_json()

       
        campos_obrigatorios = ["nome", "matricula", "idade", "data_nascimento", 
                               "nota_primeiro_semestre", "nota_segundo_semestre", 
                               "media_final", "turma_id"]

        for campo in campos_obrigatorios:
            if campo not in data:
                return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

      
        if data["nota_primeiro_semestre"] < 0 or data["nota_segundo_semestre"] < 0:
            return jsonify({"erro": "Notas não podem ser negativas"}), 400

      
        novo_aluno = {
            "id": len(alunos) + 1,
            "nome": data["nome"],
            "matricula": data["matricula"],
            "idade": data["idade"],
            "data_nascimento": data["data_nascimento"],
            "nota_primeiro_semestre": data["nota_primeiro_semestre"],
            "nota_segundo_semestre": data["nota_segundo_semestre"],
            "media_final": data["media_final"],
            "turma_id": data["turma_id"]
        }
        alunos.append(novo_aluno)
        return jsonify(novo_aluno), 200
    except Exception as e:
        return jsonify({"erro": f"Erro ao criar aluno: {str(e)}"}), 500