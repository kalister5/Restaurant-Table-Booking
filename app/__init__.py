from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from flask_login import LoginManager

bootstrap=Bootstrap()
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

def create_app(config_name):
    app= Flask(__name__)

    #Initializing flask extensions
    bootstrap.init_app(app)
    # login.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app
