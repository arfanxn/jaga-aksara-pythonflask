import os

from flask import Flask
from dotenv import load_dotenv, dotenv_values 
from .. import config
from flask_mysqldb import MySQL


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=config.get('SECRET_KEY'),
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    '''
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    '''

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    ### ROUTES ###
    @app.route('/')
    def index():
        return 'Dashboard'

    return app