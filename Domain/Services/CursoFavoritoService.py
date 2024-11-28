from Infrastructure.Repositories.CursoFavoritoRepository import get_curso_favorito_by_cpf_and_curso_id, add_curso_favorito, delete_curso_favorito, get_cursos_favoritos_by_cpf
from Domain.Entities.CursoFavorito import CursoFavorito

def get_curso_favorito_by_cpf_and_curso_id_service(cpf: str, curso_id: int) -> CursoFavorito:
    return get_curso_favorito_by_cpf_and_curso_id(cpf, curso_id)

def get_cursos_favoritos_by_cpf_service(cpf: str) -> list[CursoFavorito]:
    return get_cursos_favoritos_by_cpf(cpf)

def add_curso_favorito_service(cpf: str, curso_id: int):

    novo_favorito = CursoFavorito(
        Cpf = cpf,
        CursoId = curso_id
    )

    add_curso_favorito(novo_favorito)

def delete_curso_favorito_service(cpf: str, curso_id: int):
    delete_curso_favorito(cpf, curso_id)