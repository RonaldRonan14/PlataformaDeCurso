from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from Domain.Services.UsuarioService import get_usuario_by_cpf_service, add_usuario_service
from Domain.Services.CursoService import get_cursos_service
from werkzeug.security import check_password_hash

login_user_blueprint = Blueprint("login_user_blueprint", __name__)

@login_user_blueprint.route("/")
def index():
    try:
        cursos = get_cursos_service()

        return render_template(
            "Login/home_deslogado.html",
            cursos=cursos
        )
    except RuntimeError as e:
        abort(500, description=e)

@login_user_blueprint.route("/logar", methods=["GET", "POST"])
def login_user():
    try:
        if request.method == "GET":
            return render_template(
                "Login/login.html", 
                tipo_usuario="default"
            )
            
        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            usuario = get_usuario_by_cpf_service(username)

            if usuario and check_password_hash(usuario.Senha, password) and usuario.Banido == False:
                session["Nome"] = usuario.Nome
                session["Cpf"] = usuario.Cpf
                session["TipoUsuario"] = "default"

                return redirect(url_for("home_blueprint.index"))
            else:
                return redirect(url_for("login_user_blueprint.login_user"))
    except ValueError as e:
        return redirect(url_for("login_user_blueprint.login_user"))
    except RuntimeError as e:
        abort(500, description=e)

@login_user_blueprint.route("/cadastrar", methods=["GET", "POST"])
def cadastrar_user():
    try:
        if request.method == "GET":
            return render_template("Login/cadastrar_user.html")
        
        elif request.method == "POST":
            nome_completo = request.form["nome_completo"]
            cpf = request.form["cpf"]
            email = request.form["email"]
            password = request.form["password"]

            add_usuario_service(cpf, email, nome_completo, password)

            return redirect(url_for('login_user_blueprint.login_user'))
    except ValueError as e:
        abort(409, description=e)
    except RuntimeError as e:
        abort(500, description=e)

@login_user_blueprint.route("/logout")
def logout():
    session.pop('Nome', None)
    session.pop('TipoUsuario', None)
    return redirect(url_for("login_user_blueprint.index"))