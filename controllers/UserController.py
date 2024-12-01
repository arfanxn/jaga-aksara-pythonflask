from flask import (
    request, g, flash, render_template, redirect, session
)
from forms import (LoginForm)
from utilities.form_helpers import get_error_message, get_flashed_messages, set_form, get_form
from models import User, Otp
from enums import UserLevelEnum
from http import HTTPStatus
from pony.orm import db_session, commit


class UserController:

    def login(): 
        return render_template(
            'pages/login.jinja', 
            flashed_messages=get_flashed_messages()
        )

    def handleLogin():
        form = LoginForm(request.form) 

        if form.validate() == False: 
            flash(get_error_message(form), 'error')
            return redirect(request.referrer, code=HTTPStatus.BAD_REQUEST)
        
        country_code = form.country_code.data
        phone = form.phone.data
        
        with db_session:
            user = User.get(lambda u: (u.country_code == country_code) and (u.phone == phone))

            if user == None: 
                flash('The given phone number is not registered.', 'error')
                return redirect(request.referrer, code=HTTPStatus.NOT_FOUND)
            
            '''
            if user.level != UserLevelEnum.ADMIN.value: 
                flash('Forbidden action.', 'error')
                return redirect(request.referrer, code=HTTPStatus.FORBIDDEN)
            '''
            
            otp = Otp(user=user)
            commit()

            set_form({'country_code': country_code, 'phone': phone})

            return redirect('/otps/validate')

    def handleLogout():
        session.pop('auth', None)
        return redirect('/users/login')
