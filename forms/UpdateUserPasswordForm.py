from wtforms import Form, StringField, PasswordField, DateTimeField, SelectField, validators

genders = [
    ('female', 'female'),
    ('male', 'male'),
    ('non-binary', 'non-binary')
]

class UpdateUserPasswordForm(Form):
    current_password = password = PasswordField('Current Password', [
        validators.DataRequired(),
        validators.Length(min=8),
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo('password_confirmation')
    ])
    password_confirmation = PasswordField('Password Confirmation', [validators.DataRequired()])

