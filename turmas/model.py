from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config import db

class Turma(db.Model):
    __tablename__ = "turma"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)  

    professor = relationship("Professor", backref="turma")
    estudantes = db.relationship("Estudante", back_populates="turma")

    def __init__(self, descricao, professor_id, ativo=True):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo
        }

# EXCEÇÃO
class TurmaNaoEncontrada(Exception):
    pass

# FUNÇÕES DE SERVIÇO

def listar_turma():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def turma_por_id(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise TurmaNaoEncontrada("Turma não encontrada.")
    return turma.to_dict()

def adicionar_turma(dados):
    if not dados.get("descricao"):
        return {"error": "O campo descricao informado é obrigatório."}, 400
    if not dados.get("professor_id"):
        return {"error": "O campo professor_id informado é obrigatório."}, 400
    if dados.get("ativo") is None:
        return {"error": "O campo ativo informado é obrigatório."}, 400

    nova_turma = Turma(
        descricao=dados["descricao"],
        professor_id=dados["professor_id"],
        ativo=dados.get("ativo", True)
    )

    try:
        db.session.add(nova_turma)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"error": f"Erro ao adicionar turma: {str(e)}"}, 500

    return nova_turma.to_dict(), 201


def atualizar_turma(turma_id, novos_dados):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise TurmaNaoEncontrada("Turma não encontrada.")

    turma.descricao = novos_dados["descricao"]
    turma.professor_id = novos_dados["professor_id"]
    turma.ativo = novos_dados.get("ativo", turma.ativo)  

    db.session.commit()
    return {"message": "Turma atualizada com sucesso!"}

def excluir_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise TurmaNaoEncontrada("Turma não encontrada.")
    
    db.session.delete(turma)
    db.session.commit()
    return {"message": "Turma excluída com sucesso!"}

def resetar_turma():
    db.session.query(Turma).delete()
    db.session.commit()
