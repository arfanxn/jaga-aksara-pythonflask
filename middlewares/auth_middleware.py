from functools import wraps
from flask import request, g,abort
from flask import current_app
from models import User
from http import HTTPStatus

import jwt
import jwt.exceptions
import db

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
        unauthorized_response = {
                "message": "Unauthorized action.",
                "status": HTTPStatus.UNAUTHORIZED
            }, HTTPStatus.UNAUTHORIZED

        if "Authorization" not in request.headers:
            return unauthorized_response
        token = request.headers["Authorization"].split(" ")[1]
        try: 
            payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.exceptions.InvalidTokenError:
            return unauthorized_response
        
        db_session = db.get_session()
        user = db_session.query(User).filter_by(id=payload["user_id"]).first() #
        g.user = user

        return f(*args, **kwargs)

    return decorated