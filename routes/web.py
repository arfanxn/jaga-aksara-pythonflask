from flask import Blueprint, render_template

# Main blueprint
web_bp = Blueprint('web', __name__, url_prefix='/')

@web_bp.route('/')
def index():
    return render_template('pages/dashboard.html')

