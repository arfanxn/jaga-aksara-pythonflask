from flask import (Blueprint, g, request)
from controllers import (TransliterationController)
from middlewares.authentication_middleware import authenticate
from middlewares.app_version_middleware import check_app_version

transliteration_bp = Blueprint('transliteration', __name__, url_prefix='/transliterations')

@transliteration_bp.route('/transliterate', methods=(['POST']))
@check_app_version
@authenticate
def transliterate():
    return TransliterationController.transliterate()

@transliteration_bp.route('', methods=(['GET']))
@check_app_version
@authenticate
def get():
    if 'id' in request.args: 
        return TransliterationController.get()
    
@transliteration_bp.route('/history', methods=(['GET']))
@check_app_version
@authenticate
def history():
    return TransliterationController.history()

@transliteration_bp.route('/photo', methods=(['GET'])) # '/photo?file=md5_hash'
@check_app_version
@authenticate
def download_photo():
    return TransliterationController.download_photo()
