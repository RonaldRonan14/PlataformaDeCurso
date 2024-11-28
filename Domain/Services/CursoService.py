from Infrastructure.Repositories.CursoRepository import add_curso, get_cursos, get_curso_by_curso_id, update_curso, get_cursos_by_nome_or_descricao, desativa_curso
from Domain.Entities.Curso import Curso
import os

UPLOAD_FOLDER = 'Presentation/wwwroot/Uploads/Capa'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_cursos_service() -> list[Curso]:
    return get_cursos()

def get_curso_by_curso_id_service(curso_id: int) -> Curso:
    return get_curso_by_curso_id(curso_id)

def get_cursos_by_nome_or_descricao_service(conteudo: str) -> list[Curso]:
    return get_cursos_by_nome_or_descricao(conteudo)

def add_curso_service(nome_curso: str, descricao: str, capa_curso):
    if not nome_curso:
        raise ValueError("O nome do curso é obrigatório.")
    
    capa_path_db = ''
    
    if (capa_curso.filename != ''):
        capa_filename = f"{nome_curso}_{capa_curso.filename}"
        capa_path = f"{UPLOAD_FOLDER}/{capa_filename}"
        capa_curso.save(capa_path)
        capa_path_db = f"Uploads/Capa/{capa_filename}"

    novo_curso = Curso(
        Nome = nome_curso,
        Descricao = descricao,
        CapaPath = capa_path_db
    )

    curso_id = add_curso(novo_curso)
    
    return curso_id

def update_curso_service(curso_id: int, nome_curso: str, descricao: str, capa_curso):
    if not nome_curso:
        raise ValueError("O nome do curso é obrigatório.")
    
    capa_path_db = ''
    
    if (capa_curso.filename != ''):
        capa_filename = f"{nome_curso}_{capa_curso.filename}"
        capa_path = f"{UPLOAD_FOLDER}/{capa_filename}"
        capa_curso.save(capa_path)
        capa_path_db = f"Uploads/Capa/{capa_filename}"

    curso = Curso(
        Nome = nome_curso,
        Descricao = descricao,
        CapaPath = capa_path_db
    )

    update_curso(curso_id, curso)

def desativa_curso_service(curso_id: int):
    desativa_curso(curso_id)