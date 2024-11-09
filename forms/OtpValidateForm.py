from wtforms import Form, StringField, IntegerField, validators

class OtpValidateForm(Form):
    country_code = IntegerField('Country Code', [validators.DataRequired()])
    phone = StringField('Phone', [validators.DataRequired(), validators.Length(min=2, max=16)])
    code = IntegerField('Code', [validators.DataRequired()])
