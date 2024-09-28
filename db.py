from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine (): 
    if 'db_engine' not in g: 
        g.db_engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    return g.db_engine

def get_session(): 
    if 'db' not in g: 
        engine = get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        g.db_session = session
    return g.db_session


def close_session(error=None):
    get_session().close()