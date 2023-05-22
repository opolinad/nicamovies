from django.urls import resolve
from user.models import User
from django.http import JsonResponse

class UserExists():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if resolve(request.path_info).url_name == 'user':
            user_id = resolve(request.path_info).kwargs.get('user_id')
            try:
                user = User.objects.get(id=user_id)
                request.existent_user = user
                return self.get_response(request)
            except:
                return JsonResponse({
                    'status': False,
                    'message': 'The user with the id provided doesn\'t extist'
                }, status = 404)
        else:
            return self.get_response(request)