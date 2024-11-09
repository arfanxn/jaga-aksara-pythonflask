from flask import (Blueprint, g, request)
from controllers import (TransliterationController)
from middlewares.auth_middleware import authenticate

transliteration_bp = Blueprint('transliteration', __name__, url_prefix='/transliterations')

@transliteration_bp.route('/transliterate', methods=(['POST']))
@authenticate
def transliterate():
    return TransliterationController.transliterate()

@transliteration_bp.route('', methods=(['GET']))
@authenticate
def get():
    if 'id' in request.args: 
        return TransliterationController.get()
    
@transliteration_bp.route('/history', methods=(['GET']))
@authenticate
def history():
    return TransliterationController.history()

@transliteration_bp.route('/photo', methods=(['GET'])) # '/photo?file=md5_hash'
@authenticate
def download_photo():
    return TransliterationController.download_photo()
