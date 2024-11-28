from Config import db_context
from Domain.Entities.Curso import Curso
from datetime import datetime

class Aula(db_context.Model):
    __tablename__= 'Aulas'
    
    AulaId = db_context.Column (db_context.Integer, primary_key=True, autoincrement=True)
    CursoId = db_context.Column (db_context.Integer, db_context.ForeignKey(Curso.CursoId), nullable=False)
    Nome = db_context.Column (db_context.String (100), nullable=False)
    Descricao = db_context.Column (db_context.String(200), nullable=True)
    Complemento = db_context.Column (db_context.String, nullable=True)
    Duracao = db_context.Column(db_context.Integer, nullable=False)
    DataPublicacao = db_context.Column(db_context.Date, nullable=False, default=datetime.today())
    VideoPath = db_context.Column(db_context.String(250))