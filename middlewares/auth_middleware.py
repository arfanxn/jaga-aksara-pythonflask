from functools import wraps
from flask import request, g,abort
from flask import current_app
from models import User
from http import HTTPStatus
from pony.orm import db_session

import jwt
import jwt.exceptions
import db

def authenticate_decorated(*args, **kwargs):
    unauthorized_response = {
            "message": "Unauthorized action.",
            # "status": HTTPStatus.UNAUTHORIZED
        }, HTTPStatus.UNAUTHORIZED

    if "Authorization" not in request.headers:
        return unauthorized_response
    token = request.headers["Authorization"].split(" ")[1]
    try: 
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
    except jwt.exceptions.InvalidTokenError:
        return unauthorized_response
        
    with db_session:
        user = User.get(lambda u: u.id == payload["user_id"])
        if user is None:
            return unauthorized_response
        
        g.user = user

def authenticate(f):
    """
    A decorator to authenticate the user before the decorated view function is invoked.
    
    The decorator expects that the request contains an "Authorization" header with
    a Bearer token. The token is decoded and if it is invalid, a 401 Unauthorized
    response is returned. If the token is valid, the user is retrieved from the database
    using the user_id from the payload and the user is stored in the g object. The
    decorated view function is then invoked with the original parameters.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        response = authenticate_decorated(*args, **kwargs)
        return response if response is not None else f(*args, **kwargs)

    return decorated