from flask import (g, jsonify, request, send_file)
from forms import (TransliterateForm)
from utilities.form_helpers import get_error_message
from utilities.file_helpers import get_extension_with_dot, image_to_webp, file_exists
from utilities.hash_helpers import md5_current_timestamp
from models import Transliteration, User
from http import HTTPStatus
from pony.orm import db_session, commit, select
from db import get_db

class TransliterationController:
    def transliterate():
        form = TransliterateForm() 

        if form.validate() == False: 
            return {'message': get_error_message(form)}, HTTPStatus.BAD_REQUEST
        
        photo = form.photo.data
        saved_photo_filename = md5_current_timestamp() 
        saved_photo_ext = get_extension_with_dot(photo.filename)
        photo.save('images/temps/' + saved_photo_filename + saved_photo_ext)

        image_to_webp(
            'images/temps/' + saved_photo_filename + saved_photo_ext, 
            'images/articles/' + saved_photo_filename + '.webp', quality=85
        )

        # TODO: implements transliteration with AI model
        transliteration_result = None
        try: 
            transliteration_result = 'Lorem ipsum dolor sit amet.'
        except Exception as e:
            return {'message': 'Text transliteration failed.'}, HTTPStatus.BAD_REQUEST

        with db_session: 
            transliteration = Transliteration(
                photo = saved_photo_filename,
                result = transliteration_result,
                impression = 0,
                user = User[g.user.id]
            )
            commit()
            return transliteration.to_json(), HTTPStatus.CREATED
        
    def history():
        with db_session:
            limit = 5
            transliterations = select(a for a in Transliteration) \
                .order_by(Transliteration.created_at.desc()) \
                .limit(limit)[:limit]
            return jsonify([{
                "id": transliteration.id,
                "photo": transliteration.photo,
                "created_at" : transliteration.created_at.isoformat(),
            } for transliteration in transliterations]), HTTPStatus.OK

    def get ():
        id = request.args.get('id') # transliteration id

        with db_session:
            transliteration = select(a for a in Transliteration if a.id == id) \
                .prefetch(Transliteration.user) \
                .first()

            if transliteration == None: 
                return {'message': 'Data not found.'}, HTTPStatus.NOT_FOUND
        
            return transliteration.to_json(), HTTPStatus.OK

    def download_photo (): 
        filename = request.args.get('file')
        filepath = 'images/articles/' + filename + '.webp'
        
        if (file_exists(filepath) == False):
            return {'message': 'Data not found.'}, HTTPStatus.NOT_FOUND
        
        return send_file(filepath, as_attachment=True)