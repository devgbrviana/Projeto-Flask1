
# 📚 API de Gerenciamento Escolar

Este repositório contém a **API de Gerenciamento Escolar**, desenvolvida em **Python com Flask e SQLAlchemy**, com persistência local via SQLite.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy  
- SQLite  
- Requests  

---

## ▶️ Como Executar a API

1. **Clone o repositório**
   ```bash
   git clone https://github.com/devgbrviana/ProjetoApi-s.git
   cd ProjetoApi-s
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a API**
   ```bash
   python app.py
   ```

   A aplicação estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

📝 O banco de dados (`app.db`) será criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

### 🔸 Professor

- `GET /professor` – Lista todos os professores  
- `POST /professor` – Cria um novo professor  
- `GET /professor/<id>` – Detalha um professor  
- `PUT /professor/<id>` – Atualiza um professor  
- `DELETE /professor/<id>` – Remove um professor  

### 🔸 Turma

- `GET /turma` – Lista todas as turmas  
- `POST /turma` – Cria uma nova turma  
- `GET /turma/<id>` – Detalha uma turma  
- `PUT /turma/<id>` – Atualiza uma turma  
- `DELETE /turma/<id>` – Remove uma turma  

### 🔸 Aluno

- `GET /alunos` – Lista todos os alunos  
- `POST /alunos` – Cria um novo aluno  
- `GET /alunos/<id>` – Detalha um aluno  
- `PUT /alunos/<id>` – Atualiza um aluno  
- `DELETE /alunos/<id>` – Remove um aluno  

---

## 🔧 Exemplos de Corpo JSON

### 📄 Professor
```json
{
  "id": 2,
  "nome": "Priscilla Igreja",
  "idade": 26,
  "materia": "Desenvolvimento de APIs",
  "observacoes": "Flask"
}
```

### 📄 Turma
```json
{
  "id": 2,
  "descricao": "Desenvolvimento de APIs",
  "professor_id": 2,
  "ativo": "Ativo"
}
```

### 📄 Aluno
```json
{
  "nome": "José",
  "data_nascimento": "13/05/2005",
  "nota_primeiro_semestre": 9,
  "nota_segundo_semestre": 8,
  "turma_id": 1
}
```

---

## 📦 Estrutura do Projeto

```plaintext
ProjetoApi-s/
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
│   └── namespaces/
│       ├── aluno_namespace.py  
│       ├── professor_namespace.py 
│       └── turma_namespace.py   
│
├── TDD/
│   └── testeapp.py     
│
├── venv/                   # Ambiente virtual (não incluir no GitHub)
├── app.py                 
├── config.py 
├── Dockerfile                 
├── guardar.txt              
├── README.md                
├── requirements.txt          
├── teste.py
└── todosTDD.py
```

---

## 🛠️ Futuras Melhorias

- Implementação de autenticação em dois fatores (2FA)  
- Integração com banco de dados externo (ex: PostgreSQL)  
- Swagger completo com testes de integração  
- Interface web para gestão visual dos dados



🧑‍💻 Autor
Gabriel de Souza Viana
Arthur Mattos
Pablo Barros.
