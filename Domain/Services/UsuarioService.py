from Infrastructure.Repositories.UsuarioRepository import get_usuario_by_cpf, add_usuario, delete_usuario, update_usuario
from Domain.Entities.Usuario import Usuario
from werkzeug.security import generate_password_hash

def get_usuario_by_cpf_service(cpf: str) -> Usuario:
    return get_usuario_by_cpf(cpf)

def add_usuario_service(cpf: str, email: str, nome: str, senha: str):

    hashed_senha = generate_password_hash(senha)

    novo_usuario = Usuario(
        Cpf = cpf,
        Email = email,
        Nome = nome,
        Senha = hashed_senha
    )

    add_usuario(novo_usuario)

def update_usuario_service(cpf: str, nome: str, email: str):

    usuario = Usuario(
        Email = email,
        Nome = nome
    )

    update_usuario(cpf, usuario)

def delete_usuario_service(cpf):
    delete_usuario(cpf)