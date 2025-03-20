import unittest
import requests


class TestCrudAluno(unittest.TestCase):

    def setUp(self):
      
        requests.post('http://localhost:5000/reseta')

    def test_001_cria_aluno(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "João",
            "matricula": "12345",
            "idade": 20,
            "data_nascimento": "01/01/2001",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.0,
            "media_final": 7.75,
            "turma_id": 1
        })
        self.assertEqual(resposta.status_code, 200)
        aluno_criado = resposta.json()
        self.assertEqual(aluno_criado['nome'], 'João')
        self.assertEqual(aluno_criado['matricula'], '12345')

    def test_002_retorna_todos_alunos(self):
        resposta = requests.post('http://localhost:5000/reseta')
        requests.post('http://localhost:5000/alunos', json={
            "nome": "Maria",
            "matricula": "67890",
            "idade": 22,
            "data_nascimento": "15/05/1999",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 8.5,
            "media_final": 8.75,
            "turma_id": 1
        })
        resposta = requests.get('http://localhost:5000/alunos')
        self.assertEqual(resposta.status_code, 200)
        alunos = resposta.json()
        self.assertGreater(len(alunos), 0)
        

    def test_003_retorna_aluno_por_id(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Carlos",
            "matricula": "54321",
            "idade": 21,
            "data_nascimento": "10/10/2000",
            "nota_primeiro_semestre": 6.5,
            "nota_segundo_semestre": 7.0,
            "media_final": 6.75,
            "turma_id": 1
        })
        aluno_criado = resposta.json()
        aluno_id = aluno_criado['id']

        resposta_get = requests.get(f'http://localhost:5000/alunos/{aluno_id}')
        self.assertEqual(resposta_get.status_code, 200)
        aluno_retorno = resposta_get.json()
        self.assertEqual(aluno_retorno['id'], aluno_id)
        self.assertEqual(aluno_retorno['nome'], 'Carlos')
