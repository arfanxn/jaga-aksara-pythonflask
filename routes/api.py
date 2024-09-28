from flask import (Blueprint, g)
from controllers import UserController
from middlewares.auth_middleware import authenticate
from models import User


# Main blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Additional blueprint(s)
user_bp = Blueprint('user', __name__, url_prefix='/users')
api_bp.register_blueprint(user_bp)


@user_bp.route('/register', methods=(['POST']))
def register():
    return UserController.register()    

@user_bp.route('/login', methods=(['POST']))
def login():
    return UserController.login()    

@user_bp.route('/logout', methods=(['DELETE']))
def logout():
    return UserController.logout()    


@user_bp.route('/self', methods=(['GET']))
@authenticate
def show_self():
    return UserController.show_self()


@user_bp.route('/<int:user_id>', methods=(['PUT']))
@authenticate
def update(user_id: int):
    return UserController.update(user_id)

@user_bp.route('/self', methods=(['PUT']))
@authenticate
def update_self():
    return UserController.update(user_id=g.user.id)
