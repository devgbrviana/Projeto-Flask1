from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from datetime import date, datetime
from config import db
from turma.model import Turma
from flask import jsonify



class Estudante(db.Model):
    __tablename__ = "estudantes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date, nullable=False)
    primeira_nota = db.Column(db.Float, nullable=False)
    segunda_nota = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey("turma.id"), nullable=False)


    turma = db.relationship("Turma", back_populates="estudantes")
    
    def __init__(self, nome, turma_id, data_nascimento, primeira_nota, segunda_nota, media_final):
        self.nome = nome
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.primeira_nota = primeira_nota
        self.segunda_nota = segunda_nota
        self.media_final = media_final
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        data_nasc = self.data_nascimento
        hoje = date.today()
        idade = hoje.year - data_nasc.year

        if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
            idade -= 1

        self.idade = idade
        return idade



    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'data_nascimento': self.data_nascimento.strftime("%d/%m/%Y"),
            'primeira_nota': self.primeira_nota,
            'segunda_nota': self.segunda_nota,
            'media_final': self.media_final,
            'turma_id': self.turma_id
        }

# EXCEÇÃO
class AlunoNaoEncontrado(Exception):
    pass

# FUNÇÕES DE SERVIÇO

def aluno_por_id(aluno_id):
    aluno = Estudante.query.get(aluno_id)
    if not aluno:
        raise AlunoNaoEncontrado("Aluno não encontrado.")
    return aluno.to_dict()

def listar_alunos():
    estudantes = Estudante.query.all()
    return [e.to_dict() for e in estudantes]

def adicionar_aluno(dados):
    turma = Turma.query.get(dados["turma_id"])
    print("TURMA:", turma)
    if turma is None:
        return {"message": "Turma não encontrada"}, 404

    novo = Estudante(
        nome=dados["nome"],
        turma_id=int(dados["turma_id"]),
        data_nascimento=datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date(),
        primeira_nota=float(dados["primeira_nota"]),
        segunda_nota=float(dados["segunda_nota"]),
        media_final=(float(dados["primeira_nota"]) + float(dados["segunda_nota"])) / 2
    )

    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()),201

def atualizar_aluno(aluno_id, novos_dados):
    aluno = Estudante.query.get(aluno_id)
    if not aluno:
        raise AlunoNaoEncontrado("Aluno não encontrado.")

    aluno.nome = novos_dados["nome"]
    aluno.data_nascimento = datetime.strptime(novos_dados["data_nascimento"], "%d/%m/%Y").date()
    aluno.primeira_nota = float(novos_dados["primeira_nota"])
    aluno.segunda_nota = float(novos_dados["segunda_nota"])
    aluno.media_final = (aluno.primeira_nota + aluno.segunda_nota) / 2
    aluno.turma_id = int(novos_dados["turma_id"])
    aluno.idade = aluno.calcular_idade()

    db.session.commit()
    
    return {
        'id': aluno.id,
        'nome': aluno.nome,
        'idade': aluno.idade,
        'data_nascimento': aluno.data_nascimento,
        'primeira_nota': aluno.primeira_nota,
        'segunda_nota': aluno.segunda_nota,
        'media_final': aluno.media_final,
        'turma_id': aluno.turma_id
    }

def excluir_aluno(aluno_id):
    aluno = Estudante.query.get(aluno_id)
    if not aluno:
        raise AlunoNaoEncontrado("Aluno não encontrado.")
    
    db.session.delete(aluno)
    db.session.commit()
    return {"message": "Aluno excluído com sucesso!"}
