📚 API de Gerenciamento Escolar
Este repositório contém a API de Gerenciamento Escolar, desenvolvida com Flask e SQLAlchemy.

🚀 Tecnologias Utilizadas
Python 3.x;
Flask;
SQLAlchemy;
SQLite (como banco de dados local);
Requests (para consumo da API externa).
▶️ Como Executar a API
1. Clone o repositório
git clone https://github.com/beatrizbramont/ProjetoAPI.git
cd ProjetoAPI
2. Crie um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Instale as dependências
pip install -r requirements.txt
4. Execute a API
python app.py
A aplicação estará disponível em: 📍 http://127.0.0.1:8001

📝 Observação: O banco de dados é criado automaticamente na primeira execução.

📡 Endpoints Principais
Professor
GET /professor – Lista todas as professor
POST /professor – Cria uma nova professor
GET /professor/<id> – Detalha uma professor
PUT /professor/<id> – Atualiza uma professor
DELETE /professor/<id> – Remove uma professor
Turma
GET /turma – Lista todas as turma
POST /turma – Cria uma nova turma
GET /turma/<id> – Detalha uma turma
PUT /turma/<id> – Atualiza uma turma
DELETE /turma/<id> – Remove uma turma
Alunos
GET /alunos – Lista todas as alunos
POST /alunos – Cria uma nova alunos
GET /alunos/<id> – Detalha uma alunos
PUT /alunos/<id> – Atualiza uma alunos
DELETE /alunos/<id> – Remove uma alunos
Exemplo de corpo JSON para criação:
Professor
{
    "id":2,
    "nome":"Priscilla Igreja",
    "idade":26, 
    "materia": "Desenvolvimento de APIs",
    "observacoes": "Flask"
}
Turma
{
    "id":2,
    "descricao":"Desenvolvimento de APIs",
    "professor_id":2, 
    "ativo": "Ativo"
}
Alunos
{
    "nome": "José",
    "data_nascimento": "13/05/2005",
    "nota_primeiro_semestre": 9,
    "nota_segundo_semestre": 8,
    "turma_id": 1
}
📦 Estrutura do Projeto
reserva-de-salas-flask/
│
├── controller/
│   └── routesAlunos.py   
│   └── routesProfessor.py 
│   └── routesTurma.py    
│
├── instance/
│   └── app.db           
│
├── models/
│   └── modelAluno.py   
│   └── modelProfessor.py  
│   └── modelTurma.py  
│  
├── Swagger/
│   └── namespaces 
│           └── aluno_namespace.py  
│           └── professor_namespace.py 
│           └── turma_namespace.py   
│
├── TDD/
│   └── reseTestes.py 
│   └── testeAluno.py 
│   └── testeProfessor.py
│   └── testeTurma.py     
│
├── venv
├── app.py                    
├── config.py 
├── Dockerfile                 
├── guardar.txt              
├── README.md                
├── requirements.txt          
├── teste.py
└── todosTDD.py

🛠️ Futuras Melhorias
Autenticação em 2 fatores;
🧑‍💻 Autores
Gabriel de Souza Viana
Pablo Barros
Arthur Matos
