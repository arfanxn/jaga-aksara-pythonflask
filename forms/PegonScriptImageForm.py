from flask.wrappers import Request
from werkzeug.datastructures import FileStorage

class PegonScriptImageForm():

    image : FileStorage = None
    errors : dict[str, list[str]]|None = None

    @staticmethod
    def from_request(request : Request):
        form = PegonScriptImageForm()
        form.image = request.files.get('image')
        form.errors = {}

        return form

    def rules (self):
        return {
            'image' : {
                'required': True,
                'max' : 2 * (1024 * 1024),
                'mimes' : ['image/png', 'image/jpeg', 'image/jpg']
            }
        }
    
    def messages (self): 
        return {
            'image' : {
                'required' : 'The image file is required.',
                'max' : 'The file you uploaded exceeds the maximum allowed size of 1MB.', 
                'mimes' : 'File type not allowed. Only PNG, JPEG, and JPG files are allowed.'
            }
        }

    def validate(self):
        rules = self.rules()
        messages = self.messages()

        image = self.image

        if image is None and rules['image']['required']:
            self.errors.setdefault('image', []).append(messages['image']['required'])
            return False
        elif image.content_length > rules['image']['max']:
            self.errors.setdefault('image', []).append(messages['image']['max'])
            return False
        elif image.mimetype not in rules['image']['mimes']:
            self.errors.setdefault('image', []).append(messages['image']['mimes'])
        else:
            return True



