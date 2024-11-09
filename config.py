from os import environ
import os
from dotenv import load_dotenv
from flask import Flask
from pony.orm import Database

_is_env_loaded = False

def _load_from_env () : 
    """
    Loads environment variables from a .env file if it exists.

    If environment variables have already been loaded, this function does nothing.
    Otherwise, it loads the environment variables from a .env file if it exists.
    """
    global _is_env_loaded
    if _is_env_loaded : 
        return
    load_dotenv(override=True) 
    _is_env_loaded = True

def inject_into_app (app: Flask) : 
    """
    Loads environment variables into the given Flask app.

    This function loads environment variables from a .env file if it exists
    and injects them into the given Flask app.
    """
    _load_from_env()
    app.config.from_mapping(**dict(environ))


def inject_into_db (db: Database):
    _load_from_env()
    database_connection = os.getenv('DB_CONNECTION')
    database_name = os.getenv('DB_DATABASE')
    database_host = os.getenv('DB_HOST')
    database_port = int(os.getenv('DB_PORT') if (os.getenv('DB_PORT') != '') else 3306)
    database_username = os.getenv('DB_USERNAME')
    database_password = os.getenv('DB_PASSWORD')
    db.bind(
        provider = database_connection, 
        database = database_name,
        host = database_host, 
        user = database_username,
        password = database_password,
        port = database_port
        )
    return db
