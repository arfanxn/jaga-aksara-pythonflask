from flask import (Blueprint, g)
from controllers import (ArticleController)
from middlewares.auth_middleware import authenticate


article_bp = Blueprint('article', __name__, url_prefix='/articles')


@article_bp.route('', methods=(['POST']))
@authenticate
def store():
    return ArticleController.store()