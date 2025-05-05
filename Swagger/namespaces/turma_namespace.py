
from flask_restx import Namespace, Resource, fields
from turma.model import (
    listar_turma, turma_por_id, adicionar_turma,atualizar_turma, excluir_turma
)
turma_ns = Namespace("turma", description="Operações relacionadas as turmas")

turma_model = turma_ns.model("turma", {
    "descricao": fields.String(required=True, description="Descrição da turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor"),
    "ativo": fields.String(required=True, description="Situação da turma"),
})

turma_output_model = turma_ns.model("turmaOutput", {
    "id": fields.Integer(description="ID da turma"),
    "descricao": fields.String(description="Descrição da turma"),
    "professor_id": fields.Integer(description="ID do professor"),
    "ativo": fields.String(description="Situação da turma"),
})

@turma_ns.route("/")
class turmaResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todos as turmas"""
        return listar_turma()

    @turma_ns.expect(turma_model)
    def post(self):
        """Cria uma nova turma"""
        data = turma_ns.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@turma_ns.route("/<int:idTurma>")
class turmaIdResource(Resource):
    @turma_ns.marshal_with(turma_output_model)
    def get(self, idTurma):
        """Obtém uma turma pelo ID"""
        return turma_por_id(idTurma)

    @turma_ns.expect(turma_model)
    def put(self, idTurma):
        """Atualiza uma turma pelo ID"""
        data = turma_ns.payload
        atualizar_turma(idTurma, data)
        return data, 200

    def delete(self, idTurma):
        """Exclui uma turma pelo ID"""
        excluir_turma(idTurma)
        return {"message": "turma excluído com sucesso"}, 200
