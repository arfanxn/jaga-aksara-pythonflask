from flask import (
    request, g
)
from forms import (RegisterForm, LoginForm, UpdateUserForm)
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

    def login():
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
            
            return {'country_code': user.country_code, 'phone': user.phone}, HTTPStatus.CREATED


    def self ():
        """
        Retrieves the information of the authenticated user.

        Returns:
            tuple: A dictionary containing the user's information in JSON format 
                and an HTTP status code indicating success.
        """
        return g.user.to_json(), HTTPStatus.OK
    
    def update(user_id: int):
        form = UpdateUserForm(request.form) 

        if form.validate() == False: 
            return {'message': get_error_message(form)}, HTTPStatus.BAD_REQUEST
        
        with db_session:
            user = User.get(id=user_id) 

            if user is None:
                return {'message': 'Data not found.'}, HTTPStatus.NOT_FOUND

            user.name = form.name.data if form.name.data is not None else user.name
            user.sex = form.sex.data if form.sex.data is not None else user.sex
            user.birth_date = form.birth_date.data if form.birth_date.data is not None else user.birth_date

            return user.to_json(), HTTPStatus.OK