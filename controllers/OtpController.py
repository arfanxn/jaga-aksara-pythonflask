from flask import (
    request, current_app, render_template, redirect, flash, session
)
from forms import (OtpValidateForm, LoginForm)
from utilities.request_helpers import fire_get_and_forget
from utilities.form_helpers import get_error_message, get_flashed_messages, get_form, clear_form
from models import User, Otp
from enums import OtpStatusEnum
from http import HTTPStatus, client
from pony.orm import db_session, select, commit

class OtpController:
    def validate():
        return render_template(
            'pages/otp-validate.jinja',
            form=get_form(),
            flashed_messages=get_flashed_messages()
        )    

    def handleValidate():
        form = OtpValidateForm(request.form) 
        back_location='/otps/validate'

        country_code = form.country_code.data
        phone = form.phone.data
        code = form.code.data

        print('country_code, phone, code')
        print(country_code, phone, code)

        if form.validate() == False: 
            flash(get_error_message(form), 'error')
            return redirect(back_location, code=HTTPStatus.BAD_REQUEST)
        
        with db_session:
            result = select(
                (user, otp) 
                for user in User 
                if (user.country_code == form.country_code.data) and (user.phone == form.phone.data)
                for otp in user.otps 
                if (otp.code == form.code.data) and (otp.status == OtpStatusEnum.AVAILABLE.value)
            )[:]

            if len(result) is 0: 
                flash('Invalid code.', 'error')
                return redirect(back_location, code=HTTPStatus.NOT_FOUND)
            
            user, otp = result[0]  # Get the first (and only) result
            otp.status = OtpStatusEnum.USED.value

            clear_form()
            session['auth'] = {'id': user.id, 'user_id': user.id, 'level': user.level} # logged in user
            return redirect('/'), HTTPStatus.OK

    def handleResend():
        form = LoginForm(request.form) 

        back_location='/otps/validate'

        if form.validate() == False: 
            flash(get_error_message(form), 'error')
            return redirect(back_location, code=HTTPStatus.BAD_REQUEST)
        
        with db_session:
            user = User.get(lambda u: (u.country_code == form.country_code.data) and (u.phone == form.phone.data))

            if user is None: 
                flash('The given phone number is not registered.', 'error')
                return redirect(back_location, code=HTTPStatus.NOT_FOUND)
            
            otp = Otp(user=user)
            commit()
            
            try: 
                fire_get_and_forget('http://127.0.0.1:1010', {
                    'country_code': user.country_code,
                    'phone': user.phone
                })
            except Exception as e: # * silent the error
                print(e)
                pass
            
            flash('The otp code has been sent.', 'success')
            print('flash executed')
            return redirect(back_location, code=HTTPStatus.CREATED)