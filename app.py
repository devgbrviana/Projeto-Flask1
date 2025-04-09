# app.py
from flask import Flask
import config  # importa as configurações como módulo
from alunos.routes import alunos_bp
from professores.routes import professores_bp
from turmas.routes import turmas_bp

app = Flask(__name__)
app.config.from_object(config)  # carrega config.py

# registra os blueprints
app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )

    