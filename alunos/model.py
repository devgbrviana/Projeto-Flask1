# alunos/model.py

alunos = []
id_atual = 1

class AlunoNaoEncontrado(Exception):
    pass

def listar_alunos():
    return alunos

def aluno_por_id(id_aluno):
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            return aluno
    raise AlunoNaoEncontrado()

def adicionar_aluno(data):
    global id_atual
    data['id'] = id_atual
    id_atual += 1
    alunos.append(data)

def atualizar_aluno(id_aluno, novos_dados):
    aluno = aluno_por_id(id_aluno)
    aluno.update(novos_dados)

def excluir_aluno(id_aluno):
    aluno = aluno_por_id(id_aluno)
    alunos.remove(aluno)

def resetar_alunos():
    global alunos, id_atual
    alunos = []
    id_atual = 1