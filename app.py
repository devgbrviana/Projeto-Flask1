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
    
@app.route('/alunos/<id>', methods=['GET'])
def retorna_aluno_por_id(id):  # Método GET para retornar aluno por ID
    try:
        if not id.isdigit():
            return jsonify({"erro": "ID inválido"}), 400
        
       
        id = int(id)

        for aluno in alunos:
            if aluno["id"] == id:
                return jsonify(aluno)
        
        return jsonify({"erro": "Aluno não encontrado"}), 404
    except Exception:
        return jsonify({"erro": "Erro ao retornar aluno"}), 500


@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
      
        for aluno in alunos:
            if aluno["id"] == id:
                
                data = request.get_json()

                if "idade" in data and not isinstance(data["idade"], int):
                    return jsonify({"erro": "Idade inválida, precisa ser um número inteiro"}), 400

              
                aluno["nome"] = data.get("nome", aluno["nome"])
                aluno["matricula"] = data.get("matricula", aluno["matricula"])
                aluno["idade"] = data.get("idade", aluno["idade"])
                aluno["data_nascimento"] = data.get("data_nascimento", aluno["data_nascimento"])
                aluno["nota_primeiro_semestre"] = data.get("nota_primeiro_semestre", aluno["nota_primeiro_semestre"])
                aluno["nota_segundo_semestre"] = data.get("nota_segundo_semestre", aluno["nota_segundo_semestre"])
                aluno["media_final"] = data.get("media_final", aluno["media_final"])
                aluno["turma_id"] = data.get("turma_id", aluno["turma_id"])

                return jsonify(aluno), 200

        return jsonify({"erro": "Aluno não encontrado"}), 404

    except Exception as e:
        return jsonify({"erro": "Erro ao atualizar aluno", "detalhes": str(e)}), 500
    
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        for aluno in alunos:
            if aluno["id"] == id:
                alunos.remove(aluno)
                return jsonify({"mensagem": "Aluno deletado"})
        return jsonify({"erro": "Aluno não encontrado"}), 404
    except Exception:
        return jsonify({"erro": "Erro ao deletar aluno"}), 500
    

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas)

@app.route('/turmas', methods=['POST'])
def criar_turma():
    try:
        data = request.get_json()
        nova_turma = {
            "id": len(turmas) + 1,
            "nome": data["nome"],
            "professor_id": data["professor_id"]
        }
        turmas.append(nova_turma)
        return jsonify(nova_turma)
    except Exception:
        return jsonify({"erro": "Erro ao criar turma"})
    

@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        for turma in turmas:
            if turma["id"] == id:
                data = request.get_json()
                turma["nome"] = data.get("nome", turma["nome"])
                turma["professor_id"] = data.get("professor_id", turma["professor_id"])
                return jsonify(turma)
        return jsonify({"erro": "Turma não encontrada"}), 404
    except Exception:
        return jsonify({"erro": "Erro ao atualizar turma"}), 500
    

@app.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        for turma in turmas:
            if turma["id"] == id:
                turmas.remove(turma)
                return jsonify({"mensagem": "Turma deletada"})
        return jsonify({"erro": "Turma não encontrada"}), 404
    except Exception:
        return jsonify({"erro": "Erro ao deletar turma"}), 500
    
if __name__ == "__main__":

    app.run(debug=True)