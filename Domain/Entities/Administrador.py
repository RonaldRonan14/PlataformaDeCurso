from Config import db_context

class Administrador(db_context.Model):
    __tablename__ = 'Administradores'

    Cpf = db_context.Column (db_context.String(11), primary_key=True)
    Email = db_context.Column (db_context.String(150), nullable=False)
    Nome = db_context.Column (db_context.String(200),nullable=False)
    Senha = db_context.Column (db_context.String, nullable=False)