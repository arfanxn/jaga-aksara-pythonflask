from http import HTTPStatus
from flask import Flask, request
import singletons
import config
import db
from routes import (web_bp, api_bp)
from middlewares.app_version_middleware import check_app_version_decorated
from db import get_db
from pony.orm import db_session

app = Flask(__name__, instance_relative_config=True)

config.inject_into_app(app)
singletons.load_jaga_aksara_model()

# * database is configured in the ./models/__init__.py

app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
