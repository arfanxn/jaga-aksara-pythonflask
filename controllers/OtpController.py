from flask import (
    request, current_app
)
from forms import (OtpValidateForm, LoginForm)
from utilities.form_helpers import get_error_message
from utilities.request_helpers import fire_get_and_forget
from models import User, Otp
from enums import OtpStatusEnum
from http import HTTPStatus, client
from pony.orm import db_session, select, commit
import jwt
import threading
import requests

class OtpController:
    def validate():
        form = OtpValidateForm(request.form) 

        if form.validate() == False: 
            message = get_error_message(form)
            status = HTTPStatus.BAD_REQUEST
            return {'message': message, 'status': status}, status
        
        with db_session:
            result = select(
                (user, otp) 
                for user in User 
                if (user.country_code == form.country_code.data) and (user.phone == form.phone.data)
                for otp in user.otps 
                if (otp.code == form.code.data) and (otp.status == OtpStatusEnum.AVAILABLE.value)
            )[:]

            if len(result) is 0: 
                message = 'Invalid code.'
                status = HTTPStatus.NOT_FOUND
                return {'message': message, 'status': status}, status

            user, otp = result[0]  # Get the first (and only) result
            otp.status = OtpStatusEnum.USED.value

            token = jwt.encode(
                    {'id': user.id, 'user_id': user.id, 'level': user.level},
                    current_app.config['SECRET_KEY'],
                    algorithm='HS256'
                )

            return {'token' : token}, HTTPStatus.OK

    async def resend():
        form = LoginForm(request.form) 

        if form.validate() == False: 
            message = get_error_message(form)
            status = HTTPStatus.BAD_REQUEST
            return {'message': message, 'status': status}, status
        
        with db_session:
            user = User.get(lambda u: (u.country_code == form.country_code.data) and (u.phone == form.phone.data))

            if user is None: 
                message = 'The given phone number is not registered.'
                status = HTTPStatus.NOT_FOUND
                return {'message': message, 'status': status}, status
            
            otp = Otp(user=user)
            commit()
            
            fire_get_and_forget('http://127.0.0.1:1010', {
                'country_code': user.country_code,
                'phone': user.phone
            })
            
            return {'country_code': user.country_code, 'phone': user.phone}, HTTPStatus.CREATED
        
    