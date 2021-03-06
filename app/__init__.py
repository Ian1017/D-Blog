from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options
from flask_fontawesome import FontAwesome
from flask_uploads import UploadSet, configure_uploads, IMAGES

# Instances of flask extesnions
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()
fa = FontAwesome()
photos = UploadSet('photos', IMAGES)


def create_app(config_name):
    '''
    Function that takes configuration setting as an arguement

    Args:
    config_name: name if the configuration to be used
    '''

    # Initializing application
    app = Flask(__name__)

    # creating the app configuration
    app.config.from_object(config_options[config_name])

    # Configure Uploadset
    configure_uploads(app, photos)

    # Initialize flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    fa.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
