from Config import db_context
from datetime import datetime

class Curso(db_context.Model):
    __tablename__ = 'Cursos'

    CursoId = db_context.Column (db_context.Integer,primary_key=True)
    Nome = db_context.Column (db_context.String(100),nullable=True)
    Descricao = db_context.Column (db_context.String(200))
    DataPublicacao = db_context.Column (db_context.Date,default=datetime.today())
    Disponivel = db_context.Column(db_context.Boolean, default=True)
    CapaPath = db_context.Column(db_context.String(250))