from flask import (
    request
)
from forms import (RegisterForm)
from utilities.form_helpers import get_error_message
from models import User, Otp
from enums import UserLevelEnum
from http import HTTPStatus
from pony.orm import db_session, commit, IntegrityError
from datetime import datetime
import uuid

class UserController:

    def register():
        form = RegisterForm(request.form) 

        if form.validate() == False: 
            message = get_error_message(form)
            status = HTTPStatus.BAD_REQUEST
            return {'message': message, 'status': status}, status
        
        with db_session: 
            try:
                user_id = str(uuid.uuid4())
                user = User(id=user_id,
                        country_code=form.country_code.data,
                        phone=form.phone.data, 
                        name=form.name.data,
                        sex=form.sex.data, 
                        level=UserLevelEnum.STANDARD.value,
                        birth_date=form.birth_date.data,
                        created_at=datetime.now(),
                        updated_at=None
                        )
                otp = Otp(user=user)
                commit()

                return user.to_json(), HTTPStatus.CREATED
            except IntegrityError as e:
                message = 'The given phone number is already registered.'
                status = HTTPStatus.CONFLICT
                return {'message': message, 'status': status}, status
