# 📚 API de Gerenciamento Escolar

Este repositório contém a API de Gerenciamento Escolar, desenvolvida com Flask e SQLAlchemy.

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy  
- SQLite (como banco de dados local)  
- Requests (para consumo da API externa)

## ▶️ Como Executar a API

1. **Clone o repositório**
bash
git clone https://github.com/devgbrviana/Projeto-Flask1.git
cd Projeto-Flask1
Crie um ambiente virtual (opcional, mas recomendado)

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt
Execute a API

bash
Copiar
Editar
python app.py
A aplicação estará disponível em: http://127.0.0.1:5000

📝 O banco de dados é criado automaticamente na primeira execução.

📡 Endpoints Principais
Professor
GET /professor – Lista todos os professores

POST /professor – Cria um novo professor

GET /professor/<id> – Detalha um professor

PUT /professor/<id> – Atualiza um professor

DELETE /professor/<id> – Remove um professor

Turma
GET /turma – Lista todas as turmas

POST /turma – Cria uma nova turma

GET /turma/<id> – Detalha uma turma

PUT /turma/<id> – Atualiza uma turma

DELETE /turma/<id> – Remove uma turma

Alunos
GET /alunos – Lista todos os alunos

POST /alunos – Cria um novo aluno

GET /alunos/<id> – Detalha um aluno

PUT /alunos/<id> – Atualiza um aluno

DELETE /alunos/<id> – Remove um aluno

🔧 Exemplo de corpo JSON para criação:
Professor
json
Copiar
Editar
{
  "id": 2,
  "nome": "Priscilla Igreja",
  "idade": 26,
  "materia": "Desenvolvimento de APIs",
  "observacoes": "Flask"
}
Turma
json
Copiar
Editar
{
  "id": 2,
  "descricao": "Desenvolvimento de APIs",
  "professor_id": 2,
  "ativo": "Ativo"
}
Aluno
json
Copiar
Editar
{
  "nome": "José",
  "data_nascimento": "13/05/2005",
  "nota_primeiro_semestre": 9,
  "nota_segundo_semestre": 8,
  "turma_id": 1
}
📦 Estrutura do Projeto
arduino
Copiar
Editar
Projeto-Flask1/
│
├── controller/
│   ├── routesAlunos.py   
│   ├── routesProfessor.py 
│   └── routesTurma.py    
│
├── instance/
│   └── app.db           
│
├── models/
│   ├── modelAluno.py   
│   ├── modelProfessor.py  
│   └── modelTurma.py  
│  
├── Swagger/
│   └── namespaces 
│       ├── aluno_namespace.py  
│       ├── professor_namespace.py 
│       └── turma_namespace.py   
│
├── TDD/
│   ├── reseTestes.py 
│   ├── testeAluno.py 
│   ├── testeProfessor.py
│   └── testeTurma.py     
│
├── venv/
├── app.py                    
├── config.py 
├── Dockerfile                 
├── guardar.txt              
├── README.md                
├── requirements.txt          
├── teste.py
└── todosTDD.py
🛠️ Futuras Melhorias
Autenticação em 2 fatores

🧑‍💻 Autor
Gabriel de Souza Viana
Arthur Mattos
Pablo Barros.
