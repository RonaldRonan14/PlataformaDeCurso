from Config import db_context
from Domain.Entities.Curso import Curso

def get_cursos() -> list[Curso]:
    try:
        return db_context.session.query(Curso).filter(
            Curso.Disponivel == True
        ).limit(39).all()
    except Exception as e:
        raise RuntimeError(f"Erro ao retornar os cursos: {e}")

def get_curso_by_curso_id(curso_id: int) -> Curso:
    try:
        curso_entity = db_context.session.query(Curso).filter(
            Curso.CursoId == curso_id, 
            Curso.Disponivel == True
        ).first()

        if not curso_entity:
            raise ValueError(f"Curso com ID {curso_id} não encontrado")
        
        return curso_entity
    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar o curso {curso_id}: {e}")

def get_cursos_by_nome_or_descricao(conteudo: str) -> list[Curso]:
    try:
        return db_context.session.query(Curso).filter(
            (Curso.Nome.like(f"%{conteudo}%")) | (Curso.Descricao.like(f"%{conteudo}%")),
            Curso.Disponivel == True
        ).all()
    except Exception as e:
        raise RuntimeError(f"Erro ao retorna os cursos com conteudo {conteudo}: {e}")

def add_curso(curso: Curso) -> Curso:
    try:
        db_context.session.add(curso)
        db_context.session.commit()

        return curso.CursoId
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao inserir curso: {e}")

def update_curso(curso_id: int, curso: Curso):
    try:
        curso_entity = db_context.session.query(Curso).filter(
            Curso.CursoId == curso_id,
            Curso.Disponivel == True
        ).first()

        if not curso_entity:
            raise ValueError(f"Curso com ID {curso_id} não encontrado")

        curso_entity.Nome = curso.Nome
        curso_entity.Descricao = curso.Descricao
        if curso.CapaPath: curso_entity.CapaPath = curso.CapaPath

        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao atualizar o curso {curso_id}: {e}")

def desativa_curso(curso_id: int):
    try:
        curso_entity = db_context.session.query(Curso).filter(
            Curso.CursoId == curso_id,
            Curso.Disponivel == True
        ).first()

        if not curso_entity:
            raise ValueError(f"Curso com ID {curso_id} não encontrado")

        curso_entity.Disponivel = False

        db_context.session.commit()
    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao desativar curso {curso_id}: {e}")
