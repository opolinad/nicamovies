from django.http import JsonResponse, request
from .utils.user import get_users, create_user, get_user, update_user, delete_user
from .validators.user import is_create_user_info_valid, is_update_user_info_valid
import json


def users(request: request) -> JsonResponse:
    try:
        if request.method == 'GET':
            page_number = request.GET.get('page_number', 1)
            per_page = request.GET.get('per_page', 10)
            users = get_users(page_number, per_page)

            response_status = 200
            response = {
                'status': True,
                'data': users
            }

        elif request.method == 'POST':
            request_data = json.loads(request.body)
            name = request_data.get('name', '').lstrip()
            lastname = request_data.get('lastname', '').lstrip()
            email = request_data.get('email', '').lstrip()
            password = request_data.get('password')

            valid_request = is_create_user_info_valid(name, lastname, email, password)

            if valid_request[0]:
                response = create_user(name, lastname, email, password)
                response_status = 201
            else:
                response_status = 400
                response = {
                    'status': False,
                    'message': valid_request[1]
                }

        return JsonResponse(response, status=response_status)

    except:
        return JsonResponse({
            'status': False,
            'message': 'An error has occurred, please contact the administrator.'
        }, status=500)


def user(request: request, user_id: int) -> JsonResponse:
    try:
        response_status = 200
        if request.method == 'GET':
            response = get_user(request.existent_user)
        elif request.method == 'PUT':
            request_data = json.loads(request.body)
            name = request_data.get('name', '').lstrip()
            lastname = request_data.get('lastname', '').lstrip()
            email = request_data.get('email', '').lstrip()
            password = request_data.get('password')

            valid_request = is_update_user_info_valid(request.existent_user, name, lastname, email, password)

            if valid_request[0]:
                response = update_user(request.existent_user, name, lastname, email, password)
            else:
                response = {
                    'status': False,
                    'message': valid_request[1]
                }

        elif request.method == 'DELETE':
            response = delete_user(request.existent_user)
        else:
            response_status = 400
            response = {
                'status': False,
                'message': 'Only GET, PUT and DELETE methods allowed'
            }

        return JsonResponse(response, status=response_status)

    except:
        return JsonResponse({
            'status': False,
            'message': 'An error has occurred, please contact the administrator.'
        }, status=500)
