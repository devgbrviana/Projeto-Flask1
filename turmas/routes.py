

from flask import Blueprint, jsonify, request
from turmas.model import (
    listar_turmas, turma_por_id, adicionar_turma,
    atualizar_turma, excluir_turma, resetar_turmas,
    TurmaNaoEncontrada
)

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(listar_turmas()), 200

@turmas_bp.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        return jsonify(turma_por_id(id_turma)), 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404

@turmas_bp.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    if not dados.get("codigo") or not dados.get("professor") or not dados.get("alunos"):
        return jsonify({'erro': 'Dados obrigatórios ausentes'}), 400
    adicionar_turma(dados)
    return jsonify(dados), 200

@turmas_bp.route('/turmas/<int:id_turma>', methods=['PUT'])
def atualizar_dados_turma(id_turma):
    novos_dados = request.json
    try:
        atualizar_turma(id_turma, novos_dados)
        return jsonify(turma_por_id(id_turma)), 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404

@turmas_bp.route('/turmas/<int:id_turma>', methods=['DELETE'])
def deletar_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return '', 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404

@turmas_bp.route('/reseta-turmas', methods=['POST'])
def resetar():
    resetar_turmas()
    return '', 200