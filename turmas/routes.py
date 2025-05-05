from flask import Blueprint, jsonify, request
from turmas.model import (
    turma_por_id, adicionar_turma,
    atualizar_turma, excluir_turma, resetar_turma,
    TurmaNaoEncontrada
)

turma_bp = Blueprint('turma', __name__)


@turma_bp.route('/turma/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    turma = turma_por_id(turma_id)
    if turma:
        return jsonify(turma), 200
    return jsonify({'error': 'Turma não encontrada'}), 404


@turma_bp.route('/turma', methods=['POST'])
def criar_turma():
    dados = request.json
    if "descricao" not in dados:  # Alterar de 'nome' para 'descricao'
        return jsonify({'error': 'O campo descricao informado é obrigatório.'}), 400
    if "professor_id" not in dados:
        return jsonify({'error': 'O campo professor_id informado é obrigatório.'}), 400
    if "ativo" not in dados:
        return jsonify({'error': 'O campo ativo informado é obrigatório.'}), 400

    turma_criada, status_code = adicionar_turma(dados)
    return jsonify(turma_criada), status_code


@turma_bp.route('/turma/<int:turma_id>', methods=['PUT'])
def atualizar_dados_turma(turma_id):
    novos_dados = request.json
    try:
        atualizar_turma(turma_id, novos_dados)
        return jsonify(turma_por_id(turma_id)), 200
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada.'}), 404


@turma_bp.route('/turma/<int:turma_id>', methods=['DELETE'])
def deletar_turma(turma_id):
    try:
        excluir_turma(turma_id)
        return '', 204  # Código de sucesso para DELETE
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada.'}), 404


@turma_bp.route('/reseta-turma', methods=['POST'])
def resetar():
    resetar_turma()
    return '', 200
