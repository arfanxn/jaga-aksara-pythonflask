from wtforms import Form, StringField, PasswordField, DateTimeField, SelectField, validators

genders = [
    ('female', 'female'),
    ('male', 'male'),
    ('non-binary', 'non-binary')
]

class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=6, max=25), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])
