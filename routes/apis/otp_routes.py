from flask import (Blueprint, g)
from controllers.apis import (OtpController)
from middlewares.authentication_middleware import authenticate
from middlewares.app_version_middleware import check_app_version


otp_bp = Blueprint('otp', __name__, url_prefix='/otps')


@otp_bp.route('/validate', methods=(['POST']))
@check_app_version
def validate():
    return OtpController.validate()

@otp_bp.route('/resend', methods=(['POST']))
@check_app_version
def resend():
    return OtpController.resend()