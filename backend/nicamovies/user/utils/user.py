from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from django.http import JsonResponse
from user.models import User

def get_users(page_number, per_page=10):
    users = User.objects.get_queryset().order_by('id').values()
    paginator = Paginator(users, per_page)
    page_obj = paginator.get_page(page_number)
    try:
        users_list = list(paginator.page(page_number))
    except:
        if page_number>1:
            users_list = list(paginator.page(page_number-1))
        else:
            users_list = []

    return {
        'users':users_list,
        'count': paginator.count,
        'num_pages':paginator.num_pages
    }

def create_user(name:str, lastname:str, email:str, password:str):
    user = User.objects.create(
        name = name,
        lastname = lastname,
        email = email,
        password = make_password(password)
    )
    user_created = model_to_dict(user)
    del user_created['password']
    return {
        'status': True,
        'message': 'User created successfully',
        'user': user_created
    }

def get_user(user:User)->JsonResponse:
    return {
        'status': True,
        'message': 'User obtained successfully',
        'user': model_to_dict(user),
        'ratings': list(user.rating_set.all().values())
    }

def update_user(user:User, name:str, lastname:str, email:str, password:str)->JsonResponse:
    User.objects.filter(id=user.id).update(
        name = name,
        lastname = lastname,
        email = email,
        password = make_password(password)
    )

    user.refresh_from_db()

    return {
        'status': True,
        'message': 'User updated successfully',
        'user': model_to_dict(user)
    }

def delete_user(user:User)->JsonResponse:
    user.delete()
    return {
        'status': True,
        'message': 'User deleted successfully',
    }