from flask import (Blueprint)
from routes.apis.user_routes import user_bp
from routes.apis.otp_routes import otp_bp
from routes.apis.article_routes import article_bp
from routes.apis.transliteration_routes import transliteration_bp
from routes.apis.chat_routes import chat_bp

# Main blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Additional blueprint(s)
api_bp.register_blueprint(user_bp)
api_bp.register_blueprint(otp_bp)
api_bp.register_blueprint(article_bp)
api_bp.register_blueprint(transliteration_bp)
api_bp.register_blueprint(chat_bp)
