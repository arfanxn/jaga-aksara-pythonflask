from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class StoreTransliterationForm(FlaskForm):
    class Meta:
        csrf = False

    photo = FileField('Photo', [
        FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], message='File must be a JPG, JPEG, or PNG image.'),
    ])


