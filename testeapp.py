import unittest
import requests


class TestCrudAluno(unittest.TestCase):

    import requests
import unittest

class TestCrudAluno(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:5000'
        self.turma_id = None
        self.professor = None

        # Reset API
        resposta_reset = requests.post(f'{self.base_url}/reseta-turma')
        self.assertEqual(resposta_reset.status_code, 200)

        # Criar professor
        resposta_professor = requests.post(f'{self.base_url}/professor', json={
            "nome": "Gabriel",
            "email": "gabrielx@exemplo.com",
            "senha": "senha123",
            "data_nascimento": "20/02/2000",
            "disciplina": "Matemática",
            "ativo": True
        })
        self.assertEqual(resposta_professor.status_code, 201)
        self.professor = resposta_professor.json()
        self.assertIn('id', self.professor)

        # Criar turma
        resposta_turma = requests.post(f'{self.base_url}/turma', json={
            "descricao": "Banco de Dados SQL",
            "professor_id": self.professor["id"],
            "ativo": True
        })
        self.assertEqual(resposta_turma.status_code, 201)
        self.turma = resposta_turma.json()
        self.turma_id = self.turma.get("id")
        self.assertIsNotNone(self.turma_id, "turma_id não foi definido corretamente")

    def test_001_cria_aluno(self):
        resposta = requests.post(f'{self.base_url}/alunos', json={
            "nome": "João",
            "idade": 20,
            "data_nascimento": "03/05/2002",  # Corrigido para data válida
            "primeira_nota": 7.5,
            "segunda_nota": 8.0,
            "media_final": 7.75,
            "turma_id": self.turma_id
        })

        # Adicionando print para verificar o conteúdo da resposta
        print(resposta.status_code)  # Imprime o código de status da resposta
        print(resposta.json())       # Imprime o corpo da resposta JSON

        # Verificação
        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.json()['nome'], 'João')


    def test_002_retorna_todos_alunos(self):
        requests.post(f'{self.base_url}/alunos', json={
            "nome": "Maria",
            "idade": 22,
            "data_nascimento": "25/09/1970",
            "primeira_nota": 9.0,
            "segunda_nota": 8.5,
            "media_final": 8.75,
            "turma_id": self.turma_id
        })
        resposta = requests.get(f'{self.base_url}/alunos')
        self.assertEqual(resposta.status_code, 200)
        self.assertGreater(len(resposta.json()), 0)

    def test_003_retorna_aluno_por_id(self):
        resposta = requests.post(f'{self.base_url}/alunos', json={
            "nome": "Carlos",
            "idade": 21,
            "data_nascimento": "01/02/2002",
            "primeira_nota": 6.5,
            "segunda_nota": 7.0,
            "media_final": 6.75,
            "turma_id": self.turma_id
        })
        aluno_id = resposta.json()['id']
        resposta_get = requests.get(f'{self.base_url}/alunos/{aluno_id}')
        self.assertEqual(resposta_get.status_code, 200)
        self.assertEqual(resposta_get.json()['aluno']['nome'], 'Carlos')

    def test_004_atualiza_aluno(self):
        resposta = requests.post(f'{self.base_url}/alunos', json={
            "nome": "Felipe",
            "idade": 23,
            "data_nascimento": "10/01/2004",
            "primeira_nota": 8.0,
            "segunda_nota": 7.5,
            "media_final": 7.75,
            "turma_id": self.turma_id
        })
        aluno_id = resposta.json()['id']
        resposta_put = requests.put(f'{self.base_url}/alunos/{aluno_id}', json={
            "nome": "Felipe Silva",
            "idade": 24,
            "data_nascimento": "10/01/2004",
            "primeira_nota": 9.0,
            "segunda_nota": 8.5,
            "media_final": 8.75,
            "turma_id": self.turma_id
        })
        self.assertEqual(resposta_put.status_code, 200)
        self.assertEqual(resposta_put.json()['nome'], 'Felipe Silva')

    def test_005_deleta_aluno(self):
        resposta = requests.post(f'{self.base_url}/alunos', json={
            "nome": "Lucia",
            "idade": 19,
            "data_nascimento": "19/01/2001",
            "primeira_nota": 7.0,
            "segunda_nota": 6.5,
            "media_final": 6.75,
            "turma_id": self.turma_id
        })
        aluno_id = resposta.json()['id']
        self.assertEqual(requests.delete(f'{self.base_url}/alunos/{aluno_id}').status_code, 200)
        self.assertEqual(requests.get(f'{self.base_url}/alunos/{aluno_id}').status_code, 404)

    def test_006_id_inexistente(self):
        resposta = requests.get(f'{self.base_url}/alunos/9999')
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json()['error'], 'Aluno não encontrado')

    def test_007_id_nao_numerico(self):
        resposta = requests.get(f'{self.base_url}/alunos/abc')
        self.assertEqual(resposta.status_code, 404)

    def test_008_cria_aluno_sem_dados_obrigatorios(self):
        resposta = requests.post(f'{self.base_url}/alunos', json={
            "nome": "Pedro"
        })
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("error", resposta.json())

    def test_009_cria_varios_alunos(self):
        resposta_antes = requests.get(f'{self.base_url}/alunos')
        total_antes = len(resposta_antes.json())

        alunos = [
            {"nome": "Pedro", "idade": 18, "data_nascimento": "01/02/2004", "primeira_nota": 7, "segunda_nota": 6, "media_final": 6.5, "turma_id": self.turma_id},
            {"nome": "Leticia", "idade": 19, "data_nascimento": "05/06/2002", "primeira_nota": 8, "segunda_nota": 7, "media_final": 7.5, "turma_id": self.turma_id},
            {"nome": "Igor", "idade": 20, "data_nascimento": "02/04/2006", "primeira_nota": 9, "segunda_nota": 8, "media_final": 8.5, "turma_id": self.turma_id}
        ]

        for aluno in alunos:
            self.assertEqual(requests.post(f'{self.base_url}/alunos', json=aluno).status_code, 201)

        resposta_depois = requests.get(f'{self.base_url}/alunos')
        total_depois = len(resposta_depois.json())
        self.assertEqual(total_depois - total_antes, 3)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCrudAluno)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()