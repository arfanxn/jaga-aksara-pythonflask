from flask import (Blueprint, g)
from controllers.apis import (ChatController)
from middlewares.authentication_middleware import authenticate
from middlewares.app_version_middleware import check_app_version


chat_bp = Blueprint('chat', __name__, url_prefix='/chats')


@chat_bp.route('', methods=(['POST']))
@check_app_version
@authenticate
def store():
    return ChatController.store()

@chat_bp.route('/history', methods=(['GET']))
@check_app_version
@authenticate
def history():
    return ChatController.history()