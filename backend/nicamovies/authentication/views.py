from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, request
from authentication.validators.login import is_login_info_valid, is_register_info_valid
from datetime import datetime, timedelta
from django.utils import timezone
from user.models import User
import jwt
import environ

env = environ.Env()
environ.Env.read_env()

def login(request:request)->JsonResponse:

    if(request.method != 'POST'):
        return JsonResponse({
                    'status': False,
                    'message': 'Only POST method allowed'
                })

    email = request.POST.get('email','').lstrip()
    password = request.POST.get('password')
    valid_request = is_login_info_valid(email, password)

    if valid_request[0]:
        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                token = jwt.encode({'email': user.email, 'exp': datetime.now(timezone.utc)+timedelta(hours=1)}, env('SECRET_KEY'))

                response = {
                    'status': True,
                    'message': 'User loggged in successfully',
                    'token': token
                }

            else:
                response = {
                    'status': False,
                    'message': 'Invalid credentials'
                }

        except Exception as e:
            response = {
                'status': False,
                'message': 'Invalid credentials'
            }

    else:
        response = {
                'status': False,
                'message': valid_request[1]
            }

    return JsonResponse(response)

def register(request:request):
    if(request.method != 'POST'):
        return JsonResponse({
                    'status': False,
                    'message': 'Only POST method allowed'
                })

    email = request.POST.get('email','').lstrip()
    password = request.POST.get('password')
    name = request.POST.get('first_name','').lstrip()
    lastname = request.POST.get('last_name','').lstrip()

    valid_request = is_register_info_valid(name, lastname, email, password)

    if valid_request[0]:
        try:
            print("SECRET", env('SECRET_KEY'))
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
                print("Error", str(e))
                message= 'An error has occurred, please contact the administrator.'
            response = {
                'status': False,
                'message': message
            }
    else:
        response = {
            'status': False,
            'message': valid_request[1]
        }
    return JsonResponse(response)
