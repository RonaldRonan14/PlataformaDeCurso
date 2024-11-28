from Config import db_context
from Domain.Entities.Aula import Aula

def get_aula_by_aula_id(aula_id: int) -> Aula:
    try:
        aula_entity = db_context.session.query(Aula).filter_by(AulaId=aula_id).first()

        if not aula_entity:
            raise ValueError(f"Aula com ID {aula_id} não encontrada")

        return aula_entity
    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar a aula {aula_id}: {e}")

def get_aulas_by_curso_id(curso_id: int) -> list[Aula]:
    try:
        aulas_entity = db_context.session.query(Aula).filter(
            Aula.CursoId == curso_id
        ).all()

        return aulas_entity
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar todas as aulas do curso {curso_id}: {e}")

def add_aula(aula: Aula):
    try:
        db_context.session.add(aula)
        db_context.session.commit()
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao inserir a aula: {e}")

def update_aula(aula_id: int, aula: Aula):
    try:
        aula_entity = db_context.session.query(Aula).filter_by(AulaId=aula_id).first()
        if not aula_entity:
            raise ValueError(f"Aula com ID {aula_id} não encontrada")

        if aula_entity:
            aula_entity.Nome = aula.Nome
            aula_entity.Descricao = aula.Descricao
            aula_entity.Duracao = aula.Duracao
            db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao alterar a aula {aula_id}: {e}")

def delete_aula(aula_id: int):
    try:
        aula_entity = db_context.session.query(Aula).filter_by(AulaId=aula_id).first()
        if not aula_entity:
            raise ValueError(f"Aula com ID {aula_id} não encontrada")
        
        if aula_entity:
            db_context.session.delete(aula_entity)
            db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao deletar a aula {aula_id}: {e}")