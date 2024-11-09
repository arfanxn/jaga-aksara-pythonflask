from flask import (Blueprint, g, request)
from controllers import (ArticleController)
from middlewares.auth_middleware import authenticate


article_bp = Blueprint('article', __name__, url_prefix='/articles')

# TODO: only admin can access this route
@article_bp.route('', methods=(['POST']))
@authenticate
def store():
    return ArticleController.store()

@article_bp.route('', methods=(['GET']))
@authenticate
def get():
    if request.args.get('id') is not None: 
        return ArticleController.get()

    return ArticleController.index()

@article_bp.route('/thumbnail', methods=(['GET'])) # '/thumbnail?file=md5_hash'
@authenticate
def download_thumbnail():
    return ArticleController.download_thumbnail()

@article_bp.route('/content', methods=(['GET'])) # '/content?file=md5_hash'
@authenticate
def download_content():
    return ArticleController.download_content()