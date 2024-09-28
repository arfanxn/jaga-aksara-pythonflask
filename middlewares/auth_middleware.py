from functools import wraps
from flask import request, g,abort
from flask import current_app
from models import User
from http import HTTPStatus

import jwt
import jwt.exceptions
import db

def authenticate(f):
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