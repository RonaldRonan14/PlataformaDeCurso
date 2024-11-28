from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from Presentation.Autorize.DefaultAutorize import default_autorize
from Presentation.Autorize.AdministradorAutorize import administrador_autorize
from Domain.Services.CursoService import (
    get_cursos_service,
    get_curso_by_curso_id_service,
    add_curso_service, 
    update_curso_service, 
    desativa_curso_service
)
from Domain.Services.AulasService import (
    get_aulas_by_curso_id_service
)
from Domain.Services.CursoFavoritoService import (
    get_curso_favorito_by_cpf_and_curso_id_service,
    add_curso_favorito_service,
    delete_curso_favorito_service
)

curso_blueprint = Blueprint("curso_blueprint", __name__)

@curso_blueprint.route("/")
@default_autorize
def cursos():
    try:
        cursos = get_cursos_service()

        return render_template(
            "Curso/Cursos.html",
            cursos=cursos
        )
    except RuntimeError as e:
        abort(500, description=e)

@curso_blueprint.route("/<int:curso_id>")
@default_autorize
def index(curso_id:int):
    try:
        curso = get_curso_by_curso_id_service(curso_id)
        aulas = get_aulas_by_curso_id_service(curso_id)
        favorito = get_curso_favorito_by_cpf_and_curso_id_service(session["Cpf"], curso_id)

        duracao_total = sum([aula.Duracao for aula in aulas])

        ultima_publicacao = max((aula.DataPublicacao for aula in aulas), default=None)

        return render_template(
            "Curso/index.html", 
            curso=curso, 
            aulas=aulas,
            duracao_total=round(duracao_total, 2),
            ultima_publicacao=ultima_publicacao,
            favorito=favorito
        )
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)

@curso_blueprint.route("/add", methods=['GET','POST'])
@administrador_autorize
def add_curso():
    try:
        if request.method == 'GET':
            return render_template("Curso/Create.html")
        
        elif request.method == 'POST':
            nome_curso = request.form["nome_cusro"]
            descricao_curso = request.form["descricao_curso"]
            capa_curso = request.files["capa_curso"]
            
            curso_id = add_curso_service(nome_curso, descricao_curso, capa_curso)

            return redirect(url_for('curso_blueprint.index', curso_id=curso_id))
    except RuntimeError as e:
        abort(500, description=e)
    
@curso_blueprint.route("/update/<int:curso_id>", methods=['GET','POST'])
@administrador_autorize
def update_curso(curso_id: int):
    try:
        if request.method == 'GET':

            curso = get_curso_by_curso_id_service(curso_id)

            return render_template(
                "Curso/Update.html",
                curso=curso
            )
        
        elif request.method == 'POST':

            nome_curso = request.form["nome_cusro"]
            descricao_curso = request.form["descricao_curso"]
            capa_curso = request.files["capa_curso"]

            update_curso_service(curso_id, nome_curso, descricao_curso, capa_curso)

            return redirect(url_for('curso_blueprint.index', curso_id=curso_id))
    except RuntimeError as e:
        abort(500, description=e)
    
@curso_blueprint.route("/desativar/<int:curso_id>", methods=['POST'])
@administrador_autorize
def desativar_curso(curso_id: int):
    try:
        desativa_curso_service(curso_id)
        return redirect(url_for('home_admin_blueprint.index', curso_id=curso_id))
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)

@curso_blueprint.route("/favoritar_curso/<int:curso_id>")
@default_autorize
def favoritar_curso(curso_id: int):
    try:
        favorito = get_curso_favorito_by_cpf_and_curso_id_service(session["Cpf"], curso_id)

        if not favorito:
            add_curso_favorito_service(session["Cpf"], curso_id)
        else:
            delete_curso_favorito_service(session["Cpf"], curso_id)
        
        return redirect(url_for('curso_blueprint.index', curso_id=curso_id))
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)