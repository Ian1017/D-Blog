from flask import Flask
from config import config_options

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

    return app
