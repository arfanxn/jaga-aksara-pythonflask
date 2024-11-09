
from wtforms import Form

def get_error_message(form: Form, field_name: str = None): 
    """
    Get the first error message from a form. If `field_name` is specified,
    return the first error message from that field. Otherwise, return the
    first error message from the first field with errors.

    :param form: The form to get the error message from.
    :type form: Form
    :param field_name: The name of the field to get the error message from.
    :type field_name: str
    :return: The first error message from the form or field.
    :rtype: str
    """
    if (field_name == None):
        return list(form.errors.values())[0]
    
    return form.errors[field_name][0] 