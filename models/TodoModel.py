from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Boolean(), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=True, default=datetime.now)

