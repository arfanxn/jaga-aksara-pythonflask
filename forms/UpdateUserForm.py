from wtforms import Form, StringField, DateField, SelectField, validators
from enums import UserSexEnum

sexes = [
    (UserSexEnum.FEMALE.value, UserSexEnum.FEMALE.value),
    (UserSexEnum.MALE.value, UserSexEnum.MALE.value),
]

class UpdateUserForm(Form):
    name = StringField('Name', validators=[validators.Length(min=2, max=50)])
    sex = SelectField('Sex', validators=[], choices=sexes)
    birth_date = DateField('Birth Date', validators=[], format='%Y-%m-%d') 