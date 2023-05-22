from django.http import HttpResponse, JsonResponse, request
from .utils.movie import get_movie, create_movie, get_movie, update_movie, delete_movie
from .validators.movie import is_create_movie_info_valid
import json

def movies(request:request)->JsonResponse:
    try:
        if request.method == 'GET':
            page_number = request.GET.get('page_number', 1)
            per_page = request.GET.get('per_page', 10)
            movies = get_movies(page_number, per_page)

            response_status = 200
            response = {
                'status':True,
                'data': movies
            }

        elif request.method == 'POST':
            title = request.POST.get('title', '').lstrip()
            release_date = request.POST.get('release_date')
            genre = request.POST.get('genre', '').lstrip()
            plot = request.POST.get('plot', '').lstrip()

            valid_request = is_create_movie_info_valid(title, release_date, genre, plot)

            if valid_request[0]:
                response = create_movie(title, release_date, genre, plot)
                response_status = 201
            else:
                response_status = 400
                response = {
                    'status': False,
                    'message': valid_request[1]
                }

        return JsonResponse(response, status = response_status)

    except:
        return JsonResponse({
                'status': False,
                'message': 'An error has occurred, please contact the administrator.'
            }, status = 500)


def movie(request:request, movie_id:int)->JsonResponse:
    try:
        response_status = 200
        if request.method == 'GET':
            response = get_movie(request.movie)
        elif request.method == 'PUT':
            request_data = json.loads(request.body)
            title = request_data.get('title', '').lstrip()
            release_date = request_data.get('release_date')
            genre = request_data.get('genre', '').lstrip()
            plot = request_data.get('plot', '').lstrip()

            valid_request = is_create_movie_info_valid(title, release_date, genre, plot)

            if valid_request[0]:
                response = update_movie(request.movie, title, release_date, genre, plot)
            else:
                response = {
                    'status': False,
                    'message': valid_request[1]
                }

        elif request.method == 'DELETE':
            response = delete_movie(request.movie)
        else:
            response_status = 400
            response = {
                    'status': False,
                    'message': 'Only GET, PUT and DELETE methods allowed'
                }

        return JsonResponse(response, status = response_status)

    except:
        return JsonResponse({
                'status': False,
                'message': 'An error has occurred, please contact the administrator.'
            }, status = 500)
