from wtforms import Form, StringField, IntegerField, DateField, SelectField, validators
from enums import UserSexEnum

sexes = [
    (UserSexEnum.FEMALE.value, UserSexEnum.FEMALE.value),
    (UserSexEnum.MALE.value, UserSexEnum.MALE.value),
]

class RegisterForm(Form):
    country_code = IntegerField('Country Code', [validators.DataRequired()])
    phone = StringField('Phone', [validators.DataRequired(), validators.Length(min=2, max=16)])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    sex = SelectField('Sex', [validators.DataRequired()], choices=sexes)
    birth_date = DateField('Birth Date', [validators.DataRequired()], format='%Y-%m-%d')

