from flask import (Blueprint, g)
from controllers.apis import (UserController)
from middlewares.authentication_middleware import authenticate
from middlewares.app_version_middleware import check_app_version


user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/register', methods=(['POST']))
@check_app_version
def register():
    return UserController.register()    

@user_bp.route('/login', methods=(['POST']))
@check_app_version
def login():
    return UserController.login()    

@user_bp.route('/logout', methods=(['DELETE']))
@check_app_version
@authenticate
def logout():
    return UserController.logout()    


@user_bp.route('/self', methods=(['GET']))
@check_app_version
@authenticate
def self():
    return UserController.self()


@user_bp.route('/<int:user_id>', methods=(['PATCH']))
@check_app_version
@authenticate
def update(user_id: int):
    return UserController.update(user_id)

@user_bp.route('/self', methods=(['PATCH']))
@check_app_version
@authenticate
def update_self():
    return UserController.update(user_id=g.user.id)

