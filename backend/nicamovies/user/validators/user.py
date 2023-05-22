from django.core.validators import EmailValidator
from user.models import User
from django import forms
import re

def is_create_user_info_valid(name:str, lastname:str, email:str, password:str)->(bool, list):
    is_valid = True
    messages = []

    if not password or email == '' or name == '' or lastname == '':
        is_valid = False
        messages.append('First and last name, email and password are required')
    else:
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except forms.ValidationError:
            is_valid = False
            messages.append('Invalid email')

        existent_user = User.objects.filter(email=email)
        if len(existent_user.values()) > 0:
            is_valid = False
            messages.append('Email already registered')

        if not re.match("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
            is_valid = False
            messages.append('Invalid password, must have at least: 8 characters, one uppercase, one lowercase, one number and one special character')

    return (is_valid, '\n'.join(messages))


def is_update_user_info_valid(user:User, name:str, lastname:str, email:str, password:str)->(bool, list):
    is_valid = True
    messages = []

    if not password or email == '' or name == '' or lastname == '':
        is_valid = False
        messages.append('First and last name, email and password are required')
    else:
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except forms.ValidationError:
            is_valid = False
            messages.append('Invalid email')

        existent_user = User.objects.filter(email=email)
        if len(existent_user.values()) > 0 and existent_user[0].id != user.id:
            is_valid = False
            messages.append('Email already registered')

        if not re.match("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
            is_valid = False
            messages.append('Invalid password, must have at least: 8 characters, one uppercase, one lowercase, one number and one special character')

    return (is_valid, '\n'.join(messages))