from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from Domain.Services.AdministradorService import (
    get_administrador_by_cpf
)
from werkzeug.security import check_password_hash

login_admin_blueprint = Blueprint("login_admin_blueprint", __name__)

@login_admin_blueprint.route("/", methods=["GET", "POST"])
def login_user():
    try:
        if request.method == "GET":
            return render_template(
                "Login/login.html", 
                tipo_usuario="admin"
            )
        else:
            username = request.form["username"]
            password = request.form["password"]

            usuario = get_administrador_by_cpf(username)

            if usuario and check_password_hash(usuario.Senha, password):
                session["Nome"] = usuario.Nome
                session["Cpf"] = usuario.Cpf
                session["TipoUsuario"] = "admin"

                return redirect(url_for("home_blueprint.index"))
            else:
                return redirect(url_for("login_admin_blueprint.login_user"))
    except ValueError as e:
        return redirect(url_for("login_admin_blueprint.login_user"))
    except RuntimeError as e:
        abort(500, description=e)

@login_admin_blueprint.route("/logout")
def logout():
    session.pop('Nome', None)
    session.pop('TipoUsuario', None)
    return redirect(url_for("login_admin_blueprint.login_user"))