from Config import db_context
from sqlalchemy.orm import relationship

class Usuario(db_context.Model):
    __tablename__ = 'Usuarios'

    Cpf = db_context.Column (db_context.String(11), primary_key=True, autoincrement=False)
    Email = db_context.Column (db_context.String(150),nullable=False )
    Nome = db_context.Column (db_context.String(200), nullable=False)
    Senha = db_context.Column (db_context.String, nullable=False)
    Banido = db_context.Column (db_context.Boolean, default=False)

    cursos_favoritos = relationship(
        "Curso",
        secondary="CursosFavoritos",
        backref="usuarios_favoritaram"
    )
