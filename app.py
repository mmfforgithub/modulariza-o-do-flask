from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdt435t4654756h3q3464756y'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g1'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Usuario, Pizza, Pedido
from modulos.usuarios.usuarios import bp_usuario
from modulos.pizza.pizza import bp_pizza
app.register_blueprint(bp_usuario, url_prefix='/usuarios')
app.register_blueprint(bp_pizza, url_prefix='/pizza')