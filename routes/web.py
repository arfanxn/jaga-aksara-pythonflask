from flask import Blueprint, render_template, get_flashed_messages, flash, redirect, url_for, jsonify, current_app
from controllers import (UserController, OtpController)
from middlewares.authentication_middleware import authenticate


# Main blueprint
web_bp = Blueprint('web', __name__, url_prefix='/')

@web_bp.route('/')
@authenticate
def index():
    return render_template('pages/dashboard.jinja')

@web_bp.route('/admins/login')
def adminLogin ():
    return UserController.adminLogin()

@web_bp.route('/admins/login', methods=(['POST']))
def handleAdminLogin ():
    return UserController.handleAdminLogin()

@web_bp.route('/otps/validate')
def validateOtp ():
    return OtpController.validate()

@web_bp.route('/otps/validate', methods=['POST'])
def handleValidateOtp ():
    return OtpController.handleValidate()

@web_bp.route('/otps/resend', methods=['POST'])
def handleResendOtp ():
    return OtpController.handleResend()
