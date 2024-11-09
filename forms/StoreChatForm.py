from wtforms import Form, StringField, IntegerField, validators

class StoreChatForm(Form):
    question = StringField('Question', [validators.DataRequired()])
