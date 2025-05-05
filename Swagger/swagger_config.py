from . import api
from Swagger.namespaces.aluno_namespace import aluno_ns
from Swagger.namespaces.professores_namespace import professor_ns
from Swagger.namespaces.turma_namespace import turma_ns

# Função para registrar os namespaces
def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(aluno_ns, path="/alunos")
    api.add_namespace(professor_ns, path="/professor")
    api.add_namespace(turma_ns, path="/turma")
    api.mask_swagger = False