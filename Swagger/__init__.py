from flask_restx import Api

api = Api(
    version="1.0",
    title="API de gestão escolar",
    description="Documentação da API para alunos, turma e professores",
    doc="/docs",
    mask_swagger=False,
    prefix="/api"
)