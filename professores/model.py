from sqlalchemy import Column, String, Integer, Date
from datetime import date, datetime
from config import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date)
    disciplina = db.Column(db.String(100))
    informacoes = db.Column(db.String(255))

    turmas = db.relationship('Turma', backref='Professor', lazy=True)

    def __init__(self, nome, data_nascimento, disciplina, informacoes):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idade = self.calcular_idade()
        self.disciplina = disciplina
        self.informacoes = informacoes

    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

    def to_dict(self):
        return {
            'id': self.id,
            'data_nascimento': self.data_nascimento.strftime("%d/%m/%Y"),
            'nome': self.nome,
            'idade': self.idade,
            'disciplina': self.disciplina,
            'informacoes': self.informacoes
        }

class ProfessorNaoEncontrado(Exception):
    pass

# Funções de serviço
def listar_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def professor_por_id(professor_id):
    professor = Professor.query.get(professor_id)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado.")
    return professor.to_dict()

def adicionar_professor(dados):
    try:
        data_nascimento = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date()
    except ValueError:
        raise ValueError("Formato de data inválido. Use o formato dd/mm/aaaa.")
    
    novo_professor = Professor(
        nome=dados["nome"],
        data_nascimento=data_nascimento,
        disciplina=dados.get("disciplina"),
        informacoes=dados.get("informacoes")
    )
    
    db.session.add(novo_professor)
    db.session.commit()
    
    return novo_professor.to_dict(), 201

def atualizar_professor(professor_id, novos_dados):
    professor = Professor.query.get(professor_id)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado.")

    professor.nome = novos_dados["nome"]
    professor.data_nascimento = datetime.strptime(novos_dados["data_nascimento"], "%d/%m/%Y").date()
    professor.disciplina = novos_dados.get("disciplina", professor.disciplina)
    professor.informacoes = novos_dados.get("informacoes", professor.informacoes)
    professor.idade = professor.calcular_idade()
    db.session.commit()
    return {"message": "Professor atualizado com sucesso!"}

def excluir_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado.")
    
    db.session.delete(professor)
    db.session.commit()
    return {"message": "Professor excluído com sucesso!"}
