from flask import (
    current_app, flash, g, redirect, request, url_for, jsonify
)
import fast_ulid
import mimetypes
from http import HTTPStatus
import singletons
from forms import PegonScriptImageForm
from external_modules.jaga_aksara_ai.Integration.JagaAksara import JagaAksara



class PegonScriptController: 
    def translate ():
        # form = PegonScriptImageForm.from_request(request)
        # if form.validate() == False: 
        #     return {'errors':form.errors, 
        #             'message': list(form.errors.values())[0], 
        #             'status': HTTPStatus.UNPROCESSABLE_ENTITY}, HTTPStatus.UNPROCESSABLE_ENTITY

        file = request.files['image'] # retrieve the photo attribute from the request
        dirpath = current_app.config['JAGA_AKSARA_PEGON_SCRIPT_IMAGES_DIRECTORY']
        filename = fast_ulid.ulid()
        file_ext = mimetypes.guess_extension(file.mimetype)
        filepath = dirpath + filename + file_ext
        file.save(filepath)

        model = singletons.get_jaga_aksara_model()
        translated = model.ocr(filepath)
        
        return jsonify({
            'message': 'Script(s) translated successfully.',
            'data': {
                'translated' : translated, 
            },
            'status': HTTPStatus.OK}), HTTPStatus.OK