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


    def test_004_atualiza_aluno(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Felipe",
            "matricula": "11223",
            "idade": 23,
            "data_nascimento": "20/02/1998",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 7.5,
            "media_final": 7.75,
            "turma_id": 1
        })
        aluno_criado = resposta.json()
        aluno_id = aluno_criado['id']

        resposta_put = requests.put(f'http://localhost:5000/alunos/{aluno_id}', json={
            "nome": "Felipe Silva",
            "matricula": "11223",
            "idade": 24,
            "data_nascimento": "20/02/1997",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 8.5,
            "media_final": 8.75,
            "turma_id": 1
        })
        self.assertEqual(resposta_put.status_code, 200)
        aluno_atualizado = resposta_put.json()
        self.assertEqual(aluno_atualizado['nome'], 'Felipe Silva')
        self.assertEqual(aluno_atualizado['idade'], 24)



    def test_005_deleta_aluno(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Lucia",
            "matricula": "33445",
            "idade": 19,
            "data_nascimento": "11/11/2001",
            "nota_primeiro_semestre": 7.0,
            "nota_segundo_semestre": 6.5,
            "media_final": 6.75,
            "turma_id": 1
        })
        aluno_criado = resposta.json()
        aluno_id = aluno_criado['id']

        resposta_delete = requests.delete(f'http://localhost:5000/alunos/{aluno_id}')
        self.assertEqual(resposta_delete.status_code, 200)
        resposta_get = requests.get(f'http://localhost:5000/alunos/{aluno_id}')
        self.assertEqual(resposta_get.status_code, 404)

    def test_006_id_inexistente(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.get('http://localhost:5000/alunos/9999')
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json()['erro'], 'Aluno não encontrado')

    def test_007_atualiza_aluno_incompleto(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Gustavo",
            "matricula": "99887",
            "idade": 25,
            "data_nascimento": "05/06/1995",
            "nota_primeiro_semestre": 6.5,
            "nota_segundo_semestre": 7.0,
            "media_final": 6.75,
            "turma_id": 1
        })
        aluno_criado = resposta.json()
        aluno_id = aluno_criado['id']

        resposta_put = requests.put(f'http://localhost:5000/alunos/{aluno_id}', json={
            "nome": "Gustavo Santos"
        })
        self.assertEqual(resposta_put.status_code, 200)
        aluno_atualizado = resposta_put.json()
        self.assertEqual(aluno_atualizado['nome'], 'Gustavo Santos')
        self.assertEqual(aluno_atualizado['idade'], 25)

    def test_008_cria_aluno_sem_dados_obrigatorios(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Pedro"
        })
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("erro", resposta.json())

    def test_009_deleta_aluno_ja_deletado(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Júlia",
            "matricula": "55555",
            "idade": 19,
            "data_nascimento": "12/12/2001",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.0,
            "media_final": 7.75,
            "turma_id": 1
        })
        aluno_criado = resposta.json()
        aluno_id = aluno_criado['id']

        resposta_delete = requests.delete(f'http://localhost:5000/alunos/{aluno_id}')
        self.assertEqual(resposta_delete.status_code, 200)

        resposta_delete_repetido = requests.delete(f'http://localhost:5000/alunos/{aluno_id}')
        self.assertEqual(resposta_delete_repetido.status_code, 404)

    def test_010_lista_alunos_vazia_inicial(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.get('http://localhost:5000/alunos')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.json()), 0)

    def test_011_cria_varios_alunos(self):
        resposta = requests.post('http://localhost:5000/reseta')
        alunos_para_criar = [
            {"nome": "Aluno 1", "matricula": "111", "idade": 18, "data_nascimento": "01/01/2005", "nota_primeiro_semestre": 7, "nota_segundo_semestre": 6, "media_final": 6.5, "turma_id": 1},
            {"nome": "Aluno 2", "matricula": "222", "idade": 19, "data_nascimento": "02/02/2004", "nota_primeiro_semestre": 8, "nota_segundo_semestre": 7, "media_final": 7.5, "turma_id": 1},
            {"nome": "Aluno 3", "matricula": "333", "idade": 20, "data_nascimento": "03/03/2003", "nota_primeiro_semestre": 9, "nota_segundo_semestre": 8, "media_final": 8.5, "turma_id": 1}
        ]
        for aluno in alunos_para_criar:
            resposta = requests.post('http://localhost:5000/alunos', json=aluno)
            self.assertEqual(resposta.status_code, 200)

        resposta = requests.get('http://localhost:5000/alunos')
        self.assertEqual(len(resposta.json()), 3)

    def test_012_id_nao_numerico(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.get('http://localhost:5000/alunos/abc')
        self.assertEqual(resposta.status_code, 400)

    def test_013_atualiza_aluno_com_dados_invalidos(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Victor",
            "matricula": "77777",
            "idade": 22,
            "data_nascimento": "10/10/1998",
            "nota_primeiro_semestre": 5.5,
            "nota_segundo_semestre": 6.0,
            "media_final": 5.75,
            "turma_id": 1
        })
        aluno_criado = resposta.json()
        aluno_id = aluno_criado['id']

        resposta_put = requests.put(f'http://localhost:5000/alunos/{aluno_id}', json={
            "nome": "Victor",
            "matricula": "77777",
            "idade": "invalid"  # Dados inválidos
        })
        self.assertEqual(resposta_put.status_code, 400)

    def test_014_cria_aluno_com_nota_negativa(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Ana",
            "matricula": "98765",
            "idade": 18,
            "data_nascimento": "15/06/2004",
            "nota_primeiro_semestre": -1,  # Nota negativa
            "nota_segundo_semestre": 8.0,
            "media_final": 7.0,
            "turma_id": 1
        })
        self.assertEqual(resposta.status_code, 400)

    def test_015_cria_aluno_com_dados_incompletos(self):
        resposta = requests.post('http://localhost:5000/reseta')
        resposta = requests.post('http://localhost:5000/alunos', json={
            "nome": "Lucas",
            "matricula": "55555",
            "idade": 20,
        })
        self.assertEqual(resposta.status_code, 400)

    def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCrudAluno)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)