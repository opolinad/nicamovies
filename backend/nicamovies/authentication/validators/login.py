from django.core.validators import EmailValidator
from django import forms
import re


def is_login_info_valid(email: str, password: str) -> (bool, list):
    is_valid = True
    messages = []
    if not password or email == '':
        is_valid = False
        messages.append('Email and password are required')
    else:
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except forms.ValidationError:
            is_valid = False
            messages.append('Invalid email')

        if not re.match("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
            is_valid = False
            messages.append(
                'Invalid password, must have at least: 8 characters, one uppercase, one lowercase, one number and one special character')

    return (is_valid, '\n'.join(messages))

def is_register_info_valid(name:str, lastname:str, email:str, password:str)->(bool, list):
    valid_credentials = is_login_info_valid(email, password)
    is_valid = valid_credentials[0]
    messages = [] if valid_credentials[0] else valid_credentials[1].split('\n')

    if name == '' or lastname == '':
        is_valid = False
        messages.append('First and last name are required')

    return (is_valid, '\n'.join(messages))