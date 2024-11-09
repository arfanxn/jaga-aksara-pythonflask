from flask import Flask
import singletons
import config
import db
from routes import (web_bp, api_bp)

app = Flask(__name__, instance_relative_config=True)

config.inject_into_app(app)
singletons.load_jaga_aksara_model()

# * database is configured in the ./models/__init__.py

app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
