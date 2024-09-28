from flask import (
    current_app, flash, g, redirect, request, url_for, jsonify
)
from forms import (RegisterForm, LoginForm, UpdateUserForm)
from models import User
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from flask_bcrypt import bcrypt
import db
import json
import jwt

class UserController:

    def register():
        form = RegisterForm(request.form) 

        if form.validate() == False: 
            return {'errors':form.errors, 
                    'message': list(form.errors.values())[0], 
                    'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY
        
        user = User(name=form.name.data,
                    email=form.email.data, 
                    password=bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'), # hash the password
                    gender=form.gender.data, 
                    birth_date=form.birth_date.data)

        try:
            db_session = db.get_session()
            db_session.add(user) 
            db_session.commit()
        except IntegrityError as e:
            db_session.rollback()
            message = 'The given email is already registered.'
            return {'errors':{'email': [message] }, 
                    'message':message,
                    'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY

        return {'message': 'User registered successfully.', 'status': HTTPStatus.OK}, HTTPStatus.OK


    def login():
        form = LoginForm(request.form) 

        if form.validate() == False: 
            return {'errors':form.errors, 
                    'message': list(form.errors.values())[0], 
                    'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY
        
        db_session = db.get_session()
        user = db_session.query(User).filter_by(email=form.email.data).first()

        if user is None or bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')) is False:
            message = "The Credentials doesn't match our records." 
            return {'errors':{'email': [message] }, 
                    'message':message,
                    'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY

        token = jwt.encode(
                    {"user_id": user.id},
                    current_app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
        
        return jsonify({
            'message': 'Logged in successfully.',
            'data': {
                'user' : dict(user.to_json(), **({'token': token})),
            },
            'status': HTTPStatus.OK}), HTTPStatus.OK
    
    def logout():
        return jsonify({
            'message': 'Logged out successfully.',
            'status': HTTPStatus.OK}), HTTPStatus.OK
    
    def update(user_id: int):
        form = UpdateUserForm(request.form) 

        if form.validate() == False: 
            return {'errors': form.errors, 
                    'message': list(form.errors.values())[0], 
                    'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY
        
        db_session = db.get_session()
        user = db_session.query(User).filter_by(id=user_id).first()

        if user is None:
            return {'message': 'User not found.', 'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY

        if user.email != form.email.data :
            # check if email already exists
            exists =db_session.query(User).filter_by(id=user.id, email=form.email.data).exists()
            if exists:
                message = 'Please use a different email.'
                return {'errors':{'email': [message] }, 
                        'message':message,
                        'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY
        
        if form.name.data is not None:
                user.name = form.name.data
        if form.email.data is not None:
            user.email = form.email.data
        if form.password.data is not None:
            user.password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if form.gender.data is not None:
            user.gender = form.gender.data
        if form.birth_date.data is not None:
            user.birth_date = form.birth_date.data

        db_session.commit()

        return jsonify({
            'message': 'User updated successfully.',
            'data': {'user': user.to_json()},
            'status': HTTPStatus.OK}), HTTPStatus.OK

    def show_self():
        return jsonify({
            'message': 'Auth user retrieved successfully.',
            'data': {'user': g.user.to_json()},
            'status': HTTPStatus.OK}), HTTPStatus.OK
    