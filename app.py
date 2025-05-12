from flask import Flask, Blueprint, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db,lm
from controllers.usuario import bp_usuario_create
from models.usuario_create import bp_usuario_create
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'PIZZA'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)

# Registrando Blueprints
app.register_blueprint(bp_usuario_create, url_prefix='/user')


@app.route('/usuario_create', methods=['GET', 'POST'])
def usuario_create():
    return render_template('usuario_create.html')










