from wtforms import Form, StringField, PasswordField, DateTimeField, SelectField, validators

genders = [
    ('female', 'female'),
    ('male', 'male'),
    ('non-binary', 'non-binary')
]

class UpdateUserForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=6, max=25), validators.Email()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=genders)
    birth_date = DateTimeField('Birth Date', [validators.DataRequired()], format='%d-%m-%Y')

