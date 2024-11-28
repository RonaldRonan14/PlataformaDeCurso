import os
from flask import Flask
from Infrastructure.Conections.db import db_context
from werkzeug.security import generate_password_hash

views = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Presentation', 'Views')
static = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Presentation', 'wwwroot')

app = Flask(__name__, template_folder=views, static_folder=static)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursosdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7686412BD475C285D4BBFAD6F8185'

from Presentation.Controllers.LoginUserController import login_user_blueprint
from Presentation.Controllers.LoginAdminController import login_admin_blueprint
from Presentation.Controllers.HomeController import home_blueprint
from Presentation.Controllers.PerfilController import perfil_blueprint
from Presentation.Controllers.CursoController import curso_blueprint
from Presentation.Controllers.AulaController import aula_blueprint
from Presentation.Controllers.AdministradorController import administrador_blueprint

app.register_blueprint(login_user_blueprint, url_prefix="/")
app.register_blueprint(login_admin_blueprint, url_prefix="/login/admin")
app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(perfil_blueprint, url_prefix="/perfil")
app.register_blueprint(curso_blueprint, url_prefix="/curso")
app.register_blueprint(aula_blueprint, url_prefix="/aula")
app.register_blueprint(administrador_blueprint, url_prefix="/admin")

# Inicializa o db_context com o app
db_context.init_app(app)

with app.app_context():
    import Domain.Entities.Administrador
    import Domain.Entities.Aula
    import Domain.Entities.Curso
    import Domain.Entities.CursoFavorito
    import Domain.Entities.Usuario

    db_context.create_all()

    from Domain.Entities.Administrador import Administrador

    if not db_context.session.query(Administrador).filter_by(Cpf="00000000000").first():
        hashed_senha = generate_password_hash("FGAWAAQYtEdb")
        admin_user = Administrador(
            Cpf="00000000000",
            Nome="Administrador",
            Email="admin@example.com",
            Senha=hashed_senha
        )
        db_context.session.add(admin_user)
        db_context.session.commit()