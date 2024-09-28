from flask import Flask
import config
from routes import (web_bp, api_bp)

app = Flask(__name__, instance_relative_config=True)
config.inject_into_app(app)

app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
