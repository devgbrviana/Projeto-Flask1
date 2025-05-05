from flask import Blueprint, request, jsonify
from professores.model import (
    listar_professores, professor_por_id, adicionar_professor,
    atualizar_professor, excluir_professor, ProfessorNaoEncontrado

)

# Criando o Blueprint
professor_bp = Blueprint('professor', __name__)

# Create
@professor_bp.route('/professor', methods=['POST'])
def create_professor():
    try:
        dados = request.json
        # Chama a função que já existe em seu código
        return adicionar_professor(dados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all
@professor_bp.route("/professor", methods=['GET'])
def get_professores():
    try:
        # Chama a função que já existe em seu código
        return jsonify(listar_professores())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get by ID
@professor_bp.route('/professor/<int:professor_id>', methods=['GET'])
def get_professor_por_id(professor_id):
    try:
        return jsonify(professor_por_id(professor_id))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update
@professor_bp.route("/professor/<int:professor_id>", methods=['PUT'])
def update_professor(professor_id):
    try:
        dados = request.json
        professor_response = atualizar_professor(professor_id, dados)
        return jsonify(professor_response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete
@professor_bp.route('/professor/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    try:
        result = excluir_professor(professor_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

