from wtforms import validators, StringField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class StoreArticleForm(FlaskForm):
    class Meta:
        csrf = False

    title = StringField('Title', [validators.DataRequired(), validators.Length(min=2, max=60)])
    thumbnail = FileField('Thumbnail', [
        FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], message='File must be a JPG, JPEG, or PNG image.'),
    ])
    content = FileField('Content', [
        FileRequired(), FileAllowed(['pdf'], message='File must be a PDF.'),
    ])


