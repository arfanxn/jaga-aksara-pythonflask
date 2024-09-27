from os import environ
from dotenv import load_dotenv
from flask import Flask

_is_loaded = False

def _load_from_env () : 
    """
    Loads environment variables from a .env file if it exists.

    If environment variables have already been loaded, this function does nothing.
    Otherwise, it loads the environment variables from a .env file if it exists.
    """
    global _is_loaded
    if _is_loaded : 
        return
    load_dotenv(override=True) 
    _is_loaded = True

def inject_into_app (app: Flask) : 
    """
    Loads environment variables into the given Flask app.

    This function loads environment variables from a .env file if it exists
    and injects them into the given Flask app.
    """
    _load_from_env()
    app.config.from_mapping(**dict(environ))
    
