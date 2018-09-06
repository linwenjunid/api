from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flasgger import Swagger

db = SQLAlchemy()
sg = Swagger()
conf = Config()

login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
login_manager.login_message='请先登录。'

def create_app():
    app=Flask(__name__)
    app.config.from_object(conf)
    
    conf.init_app(app)
    db.init_app(app)
    sg.init_app(app)
    login_manager.init_app(app)

    from .v1_0 import api as v1_0_blueprint
    app.register_blueprint(v1_0_blueprint,url_prefix='/api/v1.0')

    return app
