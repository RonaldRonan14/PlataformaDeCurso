from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from Presentation.Autorize.AdministradorAutorize import administrador_autorize
from Domain.Services.AdministradorService import (
    get_administradores_service, 
    add_administrador_service, 
    get_administrador_by_cpf_service, 
    update_administrador_service, 
    delete_administrador_service
)
from Domain.Entities.Administrador import Administrador

administrador_blueprint = Blueprint("administrador_blueprint", __name__)

@administrador_blueprint.route("/")
@administrador_autorize
def index():
    try:
        administradores = get_administradores_service()

        return render_template(
            "Administrador/index.html",
            administradores=administradores
        )
    except RuntimeError as e:
        abort(500, description=e)

@administrador_blueprint.route("/add", methods=['GET', 'POST'])
@administrador_autorize
def create():
    try:
        if request.method == 'GET':
            return render_template("Administrador/Create.html")
        
        elif request.method == 'POST':
            nome_completo = request.form["nome_completo"]
            cpf = request.form["cpf"]
            email = request.form["email"]

            nova_senha = add_administrador_service(cpf, email, nome_completo)

            return render_template(
                "Administrador/Create.html", 
                nova_senha=nova_senha,
                admin=Administrador(Cpf = cpf, Nome = nome_completo, Email = email)
            )
    except ValueError as e:
        abort(409, description=e)
    except RuntimeError as e:
        abort(500, description=e)
    
@administrador_blueprint.route("/update/<cpf>", methods=['GET', 'POST'])
@administrador_autorize
def update(cpf):
    try:
        if request.method == 'GET':
            administrador = get_administrador_by_cpf_service(cpf)

            return render_template(
                "Administrador/Update.html",
                administrador=administrador
            )
        
        elif request.method == 'POST':
            nome = request.form["nome_completo"]
            email = request.form["email"]

            update_administrador_service(cpf, nome, email)

            return redirect(url_for('administrador_blueprint.index'))
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)
    
@administrador_blueprint.route("/delete/<cpf>", methods=['GET', 'POST'])
@administrador_autorize
def delete(cpf):
    try:
        if request.method == 'GET':
            administrador = get_administrador_by_cpf_service(cpf)

            return render_template(
                "Administrador/Deletar.html",
                administrador=administrador
            )
            
        elif request.method == 'POST':

            if cpf == '00000000000' : raise ValueError("O administrador padrão não pode ser deletado")

            delete_administrador_service(cpf)
            
            return redirect(url_for('administrador_blueprint.index'))
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)