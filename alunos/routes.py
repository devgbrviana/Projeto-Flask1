from flask import Blueprint, request, jsonify
from alunos.model import Estudante
from alunos.model import (
    aluno_por_id, listar_alunos, adicionar_aluno,
    atualizar_aluno, excluir_aluno, AlunoNaoEncontrado
)
from turmas.model import Turma 
from config import db

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def get_alunos():
    try:
        alunos = listar_alunos()
        return jsonify(alunos), 200
    except Exception as e:
        return jsonify({'error': f'error ao listar alunos: {str(e)}'}), 500

@alunos_bp.route('/alunos/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    try:
        aluno = aluno_por_id(aluno_id)
        turma = Turma.query.get(aluno['turma_id'])
        return jsonify({
            "aluno": aluno,
            "turma": turma.to_dict() if turma else None
        
        }), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'error ao buscar aluno: {str(e)}'}), 500

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    try:
        dados = request.get_json()
        campos_obrigatorios = ['nome', 'data_nascimento', 'primeira_nota', 'segunda_nota', 'turma_id']
        campos_faltando = [campo for campo in campos_obrigatorios if campo not in dados]

        if campos_faltando:
            return jsonify({'error': f'Campos obrigatórios ausentes: {", ".join(campos_faltando)}'}), 400

        # O adicionar_aluno já retorna um jsonify e um status
        response, status = adicionar_aluno(dados)
        return response, status

    except Exception as e:
        import traceback
        print("Mensagem:", str(e))
        traceback.print_exc()
        return jsonify({"error": "error interno ao criar aluno", "detalhes": str(e)}), 500

@alunos_bp.route('/alunos/<int:aluno_id>', methods=['PUT'])
def atualizar(aluno_id):
    try:
        dados = request.get_json()
        response = atualizar_aluno(aluno_id, dados)
        return jsonify(response), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'error ao atualizar aluno: {str(e)}'}), 500

@alunos_bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar(aluno_id):
    try:
        response = excluir_aluno(aluno_id)
        return jsonify(response), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'error ao excluir aluno: {str(e)}'}), 500

@alunos_bp.route('/reseta', methods=['POST'])
def reseta_dados():
    try:
        Estudante.query.delete()
        db.session.commit()
        return jsonify({"mensagem": "Todos os alunos foram apagados com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'error ao resetar dados: {str(e)}'}), 500
