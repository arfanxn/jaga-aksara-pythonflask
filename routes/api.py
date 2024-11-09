from flask import (Blueprint, g)
from controllers import (PegonScriptController)
from routes.apis.user_routes import user_bp
from routes.apis.otp_routes import otp_bp
from routes.apis.article_routes import article_bp


# Main blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Additional blueprint(s)
pegon_script_bp = Blueprint('pegon_script', __name__, url_prefix='/pegon-scripts')
api_bp.register_blueprint(user_bp)
api_bp.register_blueprint(otp_bp)
api_bp.register_blueprint(article_bp)
api_bp.register_blueprint(pegon_script_bp)


@pegon_script_bp.route('/translate', methods=(['POST']))
def pegon_script_translate():
    return PegonScriptController.translate()
