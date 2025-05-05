import os
from flask import Flask
from config import db
from alunos.routes import alunos_bp
from professores.routes import professor_bp
from turmas.routes import turma_bp
import config
from Swagger.swagger_config import configure_swagger

app = Flask(__name__)
config.init_app(app)  # Aqui você chama o init_app

app.register_blueprint(alunos_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)

configure_swagger(app)

with app.app_context():
    
    db.create_all()
    

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])