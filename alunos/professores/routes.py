from flask import Blueprint, jsonify, request
from professores.model import (
    listar_professores, professor_por_id, adicionar_professor,
    atualizar_professor, excluir_professor, resetar_professores,
    ProfessorNaoEncontrado
)

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(listar_professores()), 200

@professores_bp.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        return jsonify(professor_por_id(id_professor)), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404

@professores_bp.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.json
    if not dados.get("nome") or not dados.get("siape") or not dados.get("formacao"):
        return jsonify({'erro': 'Dados obrigatórios ausentes'}), 400
    adicionar_professor(dados)
    return jsonify(dados), 200

@professores_bp.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_dados_professor(id_professor):
    novos_dados = request.json
    try:
        atualizar_professor(id_professor, novos_dados)
        return jsonify(professor_por_id(id_professor)), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404

@professores_bp.route('/professores/<int:id_professor>', methods=['DELETE'])
def deletar_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return '', 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404

@professores_bp.route('/reseta-professores', methods=['POST'])
def resetar():
    resetar_professores()
    return '', 200
