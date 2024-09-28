from flask import Blueprint

# Main blueprint
web_bp = Blueprint('web', __name__, url_prefix='/')

@web_bp.route('/')
def index():
    return 'Dashboard'

