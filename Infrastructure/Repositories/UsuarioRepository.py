from Config import db_context
from Domain.Entities.Usuario import Usuario

def get_usuario_by_cpf(cpf: str) -> Usuario:
    try:
        usuario_entity = db_context.session.query(Usuario).filter_by(Cpf=cpf).first()

        if not usuario_entity:
            raise ValueError(f"Usuario com CPF {cpf} não encontrado")

        return usuario_entity
    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Erro ao retornar usuario com CPF {cpf}")

def add_usuario(usuario: Usuario):
    try:
        usuario_entity = db_context.session.query(Usuario).filter_by(Cpf=usuario.Cpf).first()

        if usuario_entity:
            raise ValueError(f"Já existe um usuário com CPF {usuario.Cpf}.")
    
        db_context.session.add(usuario)
        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao inserir o usuário: {e}")

def update_usuario(cpf: str, administrador: Usuario):
    try:
        usuario_entity = db_context.session.query(Usuario).filter_by(Cpf=cpf).first()

        if not usuario_entity:
            raise ValueError(f"Usuario com CPF {cpf} não encontrado")

        usuario_entity.Email = administrador.Email
        usuario_entity.Nome = administrador.Nome

        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao atualizar o usuário com CPF {cpf}: {e}")

def delete_usuario(cpf):
    try:
        usuario_entity = db_context.session.query(Usuario).filter_by(Cpf=cpf).first()

        if not usuario_entity:
            raise ValueError(f"Usuario com CPF {cpf} não encontrado")
        
        db_context.session.delete(usuario_entity)
        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao deletar o usuário com CPF {cpf}: {e}")