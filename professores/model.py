professores = []
id_professor_atual = 1

class ProfessorNaoEncontrado(Exception):
    pass

def listar_professores():
    return professores

def professor_por_id(id_professor):
    for professor in professores:
        if professor['id'] == id_professor:
            return professor
    raise ProfessorNaoEncontrado()

def adicionar_professor(data):
    global id_professor_atual
    data['id'] = id_professor_atual
    id_professor_atual += 1
    professores.append(data)

def atualizar_professor(id_professor, novos_dados):
    professor = professor_por_id(id_professor)
    professor.update(novos_dados)

def excluir_professor(id_professor):
    professor = professor_por_id(id_professor)
    professores.remove(professor)

def resetar_professores():
    global professores, id_professor_atual
    professores = []
    id_professor_atual = 1
