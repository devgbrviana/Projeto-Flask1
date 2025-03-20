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
