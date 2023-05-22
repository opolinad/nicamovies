from django.http import JsonResponse
from django.urls import resolve
import environ
import jwt

env = environ.Env()
environ.Env.read_env()

class AuthenticatedUser():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self.is_protected_route(request):
            try:
                token = request.headers.get('Authorization')[7:]
                jwt.decode(token, env('SECRET_KEY'), algorithms=['HS256'])
                return self.get_response(request)
            except:
                return JsonResponse({
                        'status': False,
                        'message': 'Not authorized'
                    }, status = 403)
        else:
            return self.get_response(request)

    def is_protected_route(self, request):
        return (
            (resolve(request.path_info).url_name == 'movies' and request.method != 'GET') or
            (resolve(request.path_info).url_name == 'users' and request.method != 'GET') or
            (resolve(request.path_info).url_name == 'movie' and request.method != 'GET') or
            resolve(request.path_info).url_name in ['create_rating', 'rating', 'users', 'user']
        )
