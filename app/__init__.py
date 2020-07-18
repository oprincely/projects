from flask import Flask
import os
from config import Config
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#from flask_login import LoginManager
#from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
#bootstrap = Bootstrap()

login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    #bootstrap = Bootstrap(app)
    
    
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.exams import bp as exams_bp
    app.register_blueprint(exams_bp)
    


    return app

from app import models
