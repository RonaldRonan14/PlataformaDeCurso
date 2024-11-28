
from Config import db_context
from Domain.Entities.Administrador import Administrador

def get_administradores() -> list[Administrador]:
    try:
        return db_context.session.query(Administrador).order_by(Administrador.Nome).all()
    except Exception as e:
        raise RuntimeError(f"Erro ao retorna todos os administradores: {e}")

def get_administrador_by_cpf(cpf: str) -> Administrador:
    try:
        admin_entity = db_context.session.query(Administrador).filter_by(Cpf=cpf).first()
        
        if not admin_entity:
            raise ValueError(f"Administrador com CPF {cpf} não encontrado")

        return admin_entity
    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar o administrado de cpf {cpf}: {e}")

def add_administrador(administrador: Administrador):
    try:
        existente = db_context.session.query(Administrador).filter_by(Cpf=administrador.Cpf).first()

        if existente:
            raise ValueError("Já existe um administrador com este CPF.")
    
        db_context.session.add(administrador)
        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao inserir o administrador: {e}")

def update_administrador(cpf: str, administrador: Administrador):
    try:
        admin_entity = db_context.session.query(Administrador).filter_by(Cpf=cpf).first()

        if not admin_entity:
            raise ValueError(f"Administrador com CPF {cpf} não encontrado")

        admin_entity.Email = administrador.Email
        admin_entity.Nome = administrador.Nome
        
        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao atualizar o administrador {cpf}: {e}")

def delete_administrador(cpf: str):
    try:
        admin_entity = db_context.session.query(Administrador).filter_by(Cpf=cpf).first()

        if not admin_entity:
            raise ValueError(f"Administrador com CPF {cpf} não encontrado")

        db_context.session.delete(admin_entity)
        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao deletar o administrador: {e}")