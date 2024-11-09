from flask import (Blueprint, g)
from controllers import (ChatController)
from middlewares.auth_middleware import authenticate


chat_bp = Blueprint('chat', __name__, url_prefix='/chats')


@chat_bp.route('', methods=(['POST']))
@authenticate
def store():
    return ChatController.store()

@chat_bp.route('/history', methods=(['GET']))
@authenticate
def history():
    return ChatController.history()