from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from Presentation.Autorize.DefaultAutorize import default_autorize
from Presentation.Autorize.AdministradorAutorize import administrador_autorize
from Domain.Services.AulasService import (
    add_aula_service, 
    get_aula_by_aula_id_service
)
from Domain.Services.CursoService import (
    get_curso_by_curso_id_service
)

aula_blueprint = Blueprint("aula_blueprint", __name__)

@aula_blueprint.route("/<int:aula_id>")
@default_autorize
def index(aula_id:int):
    try:
        aula = get_aula_by_aula_id_service(aula_id)
        curso = get_curso_by_curso_id_service(aula.CursoId)

        return render_template(
            "Aula/Index.html",
            aula=aula,
            curso=curso
        )
    except ValueError as e:
        abort(404, description=e)
    except RuntimeError as e:
        abort(500, description=e)

@aula_blueprint.route("/add/<int:curso_id>", methods=["GET", "POST"])
@administrador_autorize
def add_aula(curso_id:int):
    try:
        if request.method == 'GET':
            return render_template(
                "Aula/Create.html",
                curso_id=curso_id
            )
        elif request.method == 'POST':
            nome_aula = request.form["nome_aula"]
            descricao_aula = request.form["descricao_aula"]
            complemento_aula = request.form["complemento_aula"]
            video = request.files["video_aula"]

            add_aula_service(curso_id, nome_aula, descricao_aula, complemento_aula, video)

            return redirect(url_for('curso_blueprint.index', curso_id=curso_id))
    except RuntimeError as e:
        abort(500, description=e)