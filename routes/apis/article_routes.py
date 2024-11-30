from flask import (Blueprint, g, request)
from controllers.apis import (ArticleController)
from enums import UserLevelEnum
from middlewares.app_version_middleware import check_app_version
from middlewares.authentication_middleware import authenticate
from middlewares.authorization_middleware import authorize



article_bp = Blueprint('article', __name__, url_prefix='/articles')

@article_bp.route('', methods=(['POST']))
@check_app_version
@authenticate
@authorize(required_user_level=UserLevelEnum.ADMIN.value)
def store():
    return ArticleController.store()

@article_bp.route('', methods=(['GET']))
@check_app_version
def get():
    if request.args.get('id') is not None: 
        return ArticleController.get()

    return ArticleController.index()

@article_bp.route('/thumbnail', methods=(['GET'])) # '/thumbnail?file=md5_hash'
@check_app_version
def download_thumbnail():
    return ArticleController.download_thumbnail()

@article_bp.route('/content', methods=(['GET'])) # '/content?file=md5_hash'
@check_app_version
def download_content():
    return ArticleController.download_content()