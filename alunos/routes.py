

from flask import Blueprint, jsonify, request
from alunos.model import (
    listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno,
    excluir_aluno, resetar_alunos, AlunoNaoEncontrado
)

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos()), 200

@alunos_bp.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        return jsonify(aluno_por_id(id_aluno)), 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

@alunos_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json
    if not dados.get("nome") or not dados.get("matricula") or not dados.get("idade"):
        return jsonify({'erro': 'Dados obrigatórios ausentes'}), 400
    adicionar_aluno(dados)
    return jsonify(dados), 200

@alunos_bp.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_dados_aluno(id_aluno):
    novos_dados = request.json
    try:
        atualizar_aluno(id_aluno, novos_dados)
        return jsonify(aluno_por_id(id_aluno)), 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

@alunos_bp.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deletar_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

@alunos_bp.route('/reseta', methods=['POST'])
def resetar():
    resetar_alunos()
    return '', 200