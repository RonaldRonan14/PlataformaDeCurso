from functools import wraps
from flask import session, redirect, url_for, abort

def administrador_autorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'TipoUsuario' not in session:
            return redirect(url_for("login_admin_blueprint.login_user"))
        elif session["TipoUsuario"] != "admin":
            abort(403, description="Apenas administradores podem acessar esta rota.")
        return f(*args, **kwargs)
    return decorated_function
