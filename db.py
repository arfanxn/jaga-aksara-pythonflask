from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pony.orm import * 

db = None
def get_db (): 
    global db
    if db is None: 
        db = Database()
    return db