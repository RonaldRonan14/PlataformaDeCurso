from functools import wraps
from flask import session, redirect, url_for, abort

def default_autorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'TipoUsuario' not in session:
            return redirect(url_for("login_user_blueprint.index"))
        return f(*args, **kwargs)
    return decorated_function
