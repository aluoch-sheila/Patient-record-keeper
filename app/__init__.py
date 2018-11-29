from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_mail import Mail
from config import config_options
# from flask_simplemde import SimpleMDE



bootstrap = Bootstrap()# creating instances of flask extensions
db = SQLAlchemy()
# mail = Mail()
# simple = SimpleMDE()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    #instance of app
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app configurations
    app.config.from_object(config_options[config_name])
    

    # flask extensions go bellow here
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # mail.init_app(app)
    # simple.init_app(app)


    #registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
