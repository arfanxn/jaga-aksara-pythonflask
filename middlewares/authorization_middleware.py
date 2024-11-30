from functools import wraps
from flask import request, g,abort
from flask import current_app
from models import User
from enums import UserLevelEnum
from http import HTTPStatus
from pony.orm import db_session

import jwt
import jwt.exceptions
import db

def authorize_decorated(required_user_level : str):
    forbidden_response = {
            "message": "Forbidden action.",
            # "status": HTTPStatus.FORBIDDEN
        }, HTTPStatus.FORBIDDEN
            
    user = g.user

    if user is None:
        return forbidden_response

    if user.level != required_user_level:
        return forbidden_response

def authorize(required_user_level : str = UserLevelEnum.ADMIN.value):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            response = authorize_decorated(required_user_level)
            return response if response is not None else f(*args, **kwargs)
        return decorated
    return decorator