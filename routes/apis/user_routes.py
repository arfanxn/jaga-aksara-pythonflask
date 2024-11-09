from flask import (Blueprint, g)
from controllers import (UserController)
from middlewares.auth_middleware import authenticate


user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/register', methods=(['POST']))
def register():
    return UserController.register()    

@user_bp.route('/login', methods=(['POST']))
def login():
    return UserController.login()    

@user_bp.route('/logout', methods=(['DELETE']))
@authenticate
def logout():
    return UserController.logout()    


@user_bp.route('/self', methods=(['GET']))
@authenticate
def self():
    return UserController.self()


@user_bp.route('/<int:user_id>', methods=(['PATCH']))
@authenticate
def update(user_id: int):
    return UserController.update(user_id)

@user_bp.route('/self', methods=(['PATCH']))
@authenticate
def update_self():
    return UserController.update(user_id=g.user.id)

