from flask import (Blueprint, g)
from controllers import (OtpController)
from middlewares.auth_middleware import authenticate


otp_bp = Blueprint('otp', __name__, url_prefix='/otps')


@otp_bp.route('/validate', methods=(['POST']))
def validate():
    return OtpController.validate()