from flask import Blueprint, render_template, session, redirect, url_for, abort, request
from Presentation.Autorize.DefaultAutorize import default_autorize
from Domain.Services.AdministradorService import (
    get_administrador_by_cpf_service, 
    update_administrador_service
)
from Domain.Services.CursoFavoritoService import (
    get_cursos_favoritos_by_cpf_service
)
from Domain.Services.UsuarioService import (
    get_usuario_by_cpf_service, 
    delete_usuario_service, 
    update_usuario_service
)

perfil_blueprint = Blueprint("perfil_blueprint", __name__)

@perfil_blueprint.route("/")
@default_autorize
def index():
    try:
        if session['TipoUsuario'] == 'admin':
            perfil = get_administrador_by_cpf_service(session["Cpf"])
        else:
            perfil = get_usuario_by_cpf_service(session["Cpf"])
            
        cursos_favoritos = get_cursos_favoritos_by_cpf_service(session["Cpf"])

        return render_template(
            "Perfil/index.html", 
            perfil=perfil,
            cursos_favoritos=cursos_favoritos)
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)

@perfil_blueprint.route("/update", methods=['GET', 'POST'])
@default_autorize
def update():
    try:
        if request.method == 'GET':
            if session['TipoUsuario'] == 'admin':
                perfil = get_administrador_by_cpf_service(session["Cpf"])
            else:  
                perfil = get_usuario_by_cpf_service(session["Cpf"])

            return render_template(
                "Perfil/Update.html", 
                perfil=perfil
            )
        
        elif request.method == 'POST':
            nome = request.form["nome_completo"]
            email = request.form["email"]

            if session['TipoUsuario'] == 'admin':
                update_administrador_service(session["Cpf"], nome, email)
            else:
                update_usuario_service(session["Cpf"], nome, email)

            return redirect(url_for('perfil_blueprint.index'))
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)

@perfil_blueprint.route("/deletar_conta")
@default_autorize
def deletar_conta():
    try:
        delete_usuario_service(session["Cpf"])

        return redirect(url_for('login_user_blueprint.index'))
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)