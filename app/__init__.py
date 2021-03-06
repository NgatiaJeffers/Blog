from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initializing Login manager
login_manager = LoginManager()
login_manager.session_protection = 'storng'
login_manager.login_view = 'auth_login'

# Initializing Extensions
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configuration
    app.config.from_object(config_options[config_name])

    # Initalizing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the BLUEPRINT
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    return app