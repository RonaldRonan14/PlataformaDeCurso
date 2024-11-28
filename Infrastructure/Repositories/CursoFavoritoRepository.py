from Config import db_context
from Domain.Entities.CursoFavorito import CursoFavorito
from Domain.Entities.Usuario import Usuario

def get_curso_favorito_by_cpf_and_curso_id(cpf: str, curso_id: int) -> CursoFavorito:
    try:
        return db_context.session.query(CursoFavorito).filter(
            CursoFavorito.Cpf==cpf,
            CursoFavorito.CursoId==curso_id
        ).first()
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar o curso favorito pelo cpf {cpf} e curso {curso_id}: {e}")

def get_cursos_favoritos_by_cpf(cpf: str) -> list[CursoFavorito]:
    try:
        usuario = db_context.session.query(Usuario).filter_by(Cpf=cpf).first()
        if usuario:
            cursos_favoritos = usuario.cursos_favoritos
            return cursos_favoritos
        else:
            return None
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar os cursos favoritos do cpf {cpf}: {e}")

def add_curso_favorito(curso_favorito: CursoFavorito):
    try:
        db_context.session.add(curso_favorito)
        db_context.session.commit()
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao inserir o curso nos favoritos: {e}")

def delete_curso_favorito(cpf: str, curso_id: int):
    try:
        curso_favorito = db_context.session.query(CursoFavorito).filter(
            CursoFavorito.Cpf==cpf,
            CursoFavorito.CursoId==curso_id
        ).first()
        
        if not curso_favorito:
            raise ValueError("Curso favorito não encontrado")
        
        db_context.session.delete(curso_favorito)
        db_context.session.commit()

    except ValueError as e:
        raise
    except Exception as e:
        db_context.session.rollback()
        raise RuntimeError(f"Erro ao deletar o curso favorito: {e}")