from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from Presentation.Autorize.DefaultAutorize import default_autorize
from Domain.Services.CursoService import (
    get_cursos_service, 
    get_cursos_by_nome_or_descricao_service
)
from Domain.Services.CursoFavoritoService import (
    get_cursos_favoritos_by_cpf_service
)

home_blueprint = Blueprint("home_blueprint", __name__)

@home_blueprint.route("/")
@default_autorize
def index():
    try:
        cursos = get_cursos_service()

        if session["TipoUsuario"] == 'admin':
            return render_template(
                'Home/home_logado.html', 
                cursos = cursos
            )
        else:
            cursos_favoritos = get_cursos_favoritos_by_cpf_service(session["Cpf"])

            return render_template(
                'Home/home_logado_user.html', 
                cursos = cursos,
                cursos_favoritos=cursos_favoritos
            )
    except RuntimeError as e:
        abort(500, description=e)
    

@home_blueprint.route("/filtro", methods=['GET'])
@default_autorize
def filtro():
    try:
        conteudo = request.args.get("conteudo", "")
        
        if not conteudo:
            return redirect(url_for("home_blueprint.index"))
        
        cursos = get_cursos_by_nome_or_descricao_service(conteudo)

        return render_template(
            "Home/home_logado.html", 
            cursos = cursos
        )
    except RuntimeError as e:
        abort(500, description=e)