from flask import Flask
from config import config_options
from flask_fontawesome import FontAwesome

fa = FontAwesome

def create_app(config_name):
    '''
    Function that takes configuration setting as an arguement

    Args:
    config_name: name if the configuration to be used
    '''

    # Initializing application
    app = Flask(__name__)

    #creating the app configuration
    app.config.from_object(config_options[config_name])

    #Initialize flask extensions
    ##fa.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
   
    return app
