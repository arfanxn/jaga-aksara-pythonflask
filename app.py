import os

from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from models import User

from sqlalchemy.sql import func

app = Flask(__name__, instance_relative_config=True)
config.inject_into_app(app)
db = SQLAlchemy(app)

with app.app_context():
    try:
        db.engine.connect()
        print("Connection successful!")
        db.create_all()
        print("Creation successful!")

    except Exception as e:
        print(f"Connection failed: {e}")


### ROUTES ### 
@app.route('/')
def index():
    return 'Dashboard'