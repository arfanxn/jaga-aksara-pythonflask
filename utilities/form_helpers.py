from flask import get_flashed_messages as _get_flashed_messages, session
from wtforms import Form

def set_form(form): 
    session['form'] = form

def get_form(key: str = None): 
    form = session.get('form')
    if key != None and key in form: 
        return form[key]
    return form

def clear_form(): 
    session.pop('form', None)

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

def get_flashed_messages():
    """
    Retrieve flashed messages organized by category.

    This function fetches flashed messages with categories and organizes
    them into a dictionary where each key is a category and the value is
    a list of messages belonging to that category.

    :return: A dictionary of messages categorized by their category.
    :rtype: dict
    """

    flashed_messages = _get_flashed_messages(with_categories=True)

    messages_by_category = {}
    
    for category, message in flashed_messages:
        if category not in messages_by_category:
            messages_by_category[category] = []
        messages_by_category[category].append(message)
    
    return messages_by_category;

def get_flashed_error_message():
    """
    Retrieve the first flashed error message, if available.

    This function checks for flashed messages under the 'error' category
    and returns the first message found. If there are no messages in the
    'error' category, it will check the 'message' category instead. If
    no messages are found in either category, it returns None.

    :return: The first flashed error message or None if no error messages
            are present.
    :rtype: str or None
    """
    messages = get_flashed_messages().get('error', None) 
    if (messages == None):  
        messages = get_flashed_messages().get('message')

    if (messages == None):
        return None
    elif (isinstance(messages, str)): 
        return messages
    elif (isinstance(messages[0], str)): 
        return messages[0]
    elif (isinstance(messages[0][0], str)): 
        return messages[0][0]
