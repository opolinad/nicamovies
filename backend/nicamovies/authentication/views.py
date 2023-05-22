from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, request
from authentication.validators.login import is_login_info_valid, is_register_info_valid
from datetime import datetime, timedelta
from django.utils import timezone
from user.models import User
import jwt
import json
import environ

env = environ.Env()
environ.Env.read_env()

def login(request:request)->JsonResponse:

    if(request.method != 'POST'):
        return JsonResponse({
                    'status': False,
                    'message': 'Only POST method allowed'
                }, status = 400)

    request_data = json.loads(request.body)
    email = request_data.get('email','').lstrip()
    password = request_data.get('password')
    valid_request = is_login_info_valid(email, password)

    response_status = 200

    if valid_request[0]:
        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                token = jwt.encode({'email': user.email, 'exp': datetime.now(timezone.utc)+timedelta(days=7)}, env('SECRET_KEY'))

                response = {
                    'status': True,
                    'message': 'User loggged in successfully',
                    'token': token
                }

            else:
                response_status = 400
                response = {
                    'status': False,
                    'message': 'Invalid credentials'
                }

        except:
            response_status = 400
            response = {
                'status': False,
                'message': 'Invalid credentials'
            }

    else:
        response_status = 400
        response = {
                'status': False,
                'message': valid_request[1]
            }

    return JsonResponse(response, status = response_status)

def register(request:request):
    print("Entra")
    if(request.method != 'POST'):
        return JsonResponse({
                    'status': False,
                    'message': 'Only POST method allowed'
                }, status = 400)

    request_data = json.loads(request.body)
    email = request_data.get('email','').lstrip()
    password = request_data.get('password')
    name = request_data.get('first_name','').lstrip()
    lastname = request_data.get('last_name','').lstrip()

    response_status = 201

    valid_request = is_register_info_valid(name, lastname, email, password)

    if valid_request[0]:
        try:
            user = User.objects.create(
                    name = name,
                    lastname = lastname,
                    email = email,
                    password = make_password(password)
                )
            token = jwt.encode({
                    'email': user.email,
                    'exp': datetime.now(timezone.utc)+timedelta(days=7)
                },
                env('SECRET_KEY')
            )
            response = {
                'status': True,
                'message': 'User registered successfully',
                'token': token
            }

        except Exception as e:
            if 'UNIQUE' in str(e) and 'email' in str(e):
                message= 'Email is already registered'
            else:
                message= 'An error has occurred, please contact the administrator.'
            response_status = 400
            response = {
                'status': False,
                'message': message
            }
    else:
        response_status = 400
        response = {
            'status': False,
            'message': valid_request[1]
        }
    return JsonResponse(response, status = response_status)
