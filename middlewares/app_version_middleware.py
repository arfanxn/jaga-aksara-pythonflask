from functools import wraps
from flask import request
from http import HTTPStatus
from pony.orm import db_session


from db import get_db

def check_app_version_decorated(*args, **kwargs):
    not_acceptable_response = {
            'message': 'Request is not acceptable due to mismatch app-version.',
        }, HTTPStatus.NOT_ACCEPTABLE

    header_name = 'app-version'

    if header_name not in request.headers:
        return not_acceptable_response
    
    app_version = int(request.headers[header_name])

    with db_session:
        db = get_db()
        sql_query = "SELECT * FROM updates ORDER BY created_at DESC LIMIT 1"
        cursor = db.execute(sql_query)
        result = cursor.fetchone()
        column_names = [description[0] for description in cursor.description]
        row = {}
        if result is None:
            return not_acceptable_response

        for column, value in zip(column_names, result):
            row[column] = value

        if int(row['version']) != app_version: 
            return not_acceptable_response

def check_app_version(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        response =  check_app_version_decorated(*args, **kwargs)
        return response if response is not None else f(*args, **kwargs)

    return decorated