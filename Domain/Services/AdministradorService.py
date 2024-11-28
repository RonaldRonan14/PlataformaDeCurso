from Infrastructure.Repositories.AdministradorRepository import get_administrador_by_cpf, add_administrador, get_administradores, update_administrador, delete_administrador
from Domain.Entities.Administrador import Administrador
from werkzeug.security import generate_password_hash
import random
import string

def get_administradores_service() -> list[Administrador]:
    return get_administradores()

def get_administrador_by_cpf_service(cpf:str) -> Administrador:
    return get_administrador_by_cpf(cpf)

def add_administrador_service(cpf: str, email: str, nome: str) -> str:
    if not cpf or not email or not nome:
        raise ValueError("Todos os campos são obrigatórios.")
    
    nova_senha = gerar_senha(12)
    
    hashed_senha = generate_password_hash(nova_senha)

    novo_admin = Administrador(
        Cpf = cpf,
        Email = email,
        Nome = nome,
        Senha = hashed_senha
    )

    add_administrador(novo_admin)

    return nova_senha

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def update_administrador_service(cpf: str, nome: str, email: str):

    admin = Administrador(
        Email = email,
        Nome = nome
    )

    update_administrador(cpf, admin)

def delete_administrador_service(cpf: str):
    delete_administrador(cpf)