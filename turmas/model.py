

turmas = []
id_turma_atual = 1

class TurmaNaoEncontrada(Exception):
    pass

def listar_turmas():
    return turmas

def turma_por_id(id_turma):
    for turma in turmas:
        if turma['id'] == id_turma:
            return turma
    raise TurmaNaoEncontrada()

def adicionar_turma(data):
    global id_turma_atual
    data['id'] = id_turma_atual
    id_turma_atual += 1
    turmas.append(data)

def atualizar_turma(id_turma, novos_dados):
    turma = turma_por_id(id_turma)
    turma.update(novos_dados)

def excluir_turma(id_turma):
    turma = turma_por_id(id_turma)
    turmas.remove(turma)

def resetar_turmas():
    global turmas, id_turma_atual
    turmas = []
    id_turma_atual = 1