from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def init_app(app):
    app.config['HOST'] = '0.0.0.0'
    app.config['PORT'] = 5000
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    db.init_app(app)  # Inicializa SQLAlchemy com a app Flask
