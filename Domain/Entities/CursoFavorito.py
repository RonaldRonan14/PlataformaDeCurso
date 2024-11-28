from Config import db_context
from Domain.Entities.Curso import Curso
from Domain.Entities.Usuario import Usuario

class CursoFavorito(db_context.Model):
    __tablename__= 'CursosFavoritos'
    
    Cpf = db_context.Column (db_context.String(11), db_context.ForeignKey(Usuario.Cpf), primary_key=True, autoincrement=False, nullable=False)
    CursoId = db_context.Column (db_context.Integer, db_context.ForeignKey(Curso.CursoId), primary_key=True, autoincrement=False, nullable=False)