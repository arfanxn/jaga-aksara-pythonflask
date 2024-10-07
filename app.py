from flask import Flask
import external_modules
import config
from routes import (web_bp, api_bp)

app = Flask(__name__, instance_relative_config=True)
config.inject_into_app(app)

# Load external module
external_modules.load_jaga_aksara_model()

app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
