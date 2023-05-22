from django.http import HttpResponse, JsonResponse, request
from .utils.movie import get_movies, create_movie, get_movie, update_movie, delete_movie, create_rating_for, update_rating, delete_rating
from .validators.movie import is_create_movie_info_valid, is_create_rating_info_valid
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
            request_data = json.loads(request.body)
            title = request_data.get('title', '').lstrip()
            release_date = request_data.get('release_date')
            genre = request_data.get('genre', '').lstrip()
            plot = request_data.get('plot', '').lstrip()

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
                response_status = 400
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

def create_rating(request:request, movie_id:int, user_id:int)->JsonResponse:
    try:
        if request.method != 'POST':
            response_status = 400
            return JsonResponse({
                'status': False,
                'message': 'Only POST method allowed'
            }, status=400)

        if (len(request.body) == 0):
            return JsonResponse({
                'status': False,
                'message': 'No information received'
            }, status=400)

        request_data = json.loads(request.body)
        rating = request_data.get('rating')
        comment = request_data.get('comment', '').lstrip()

        valid_request = is_create_rating_info_valid(rating, comment, movie_id, user_id)

        if valid_request[0]:
            response_status = 201
            response = create_rating_for(movie_id, user_id, rating, comment)
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

def rating(request:request, rating_id:int)->JsonResponse:
    try:
        if request.method == 'PUT':
            request_data = json.loads(request.body)
            rating = request_data.get('rating')
            comment = request_data.get('comment', '').lstrip()

            valid_request = is_create_rating_info_valid(rating, comment)

            if valid_request[0]:
                response = update_rating(request.rating, rating, comment)
                response_status = 200
            else:
                response_status = 400
                response = {
                    'status': False,
                    'message': valid_request[1]
                }
        elif request.method == 'DELETE':
            response = delete_rating(request.rating)
            response_status = 200
        else:
            response_status = 400
            response = {
                    'status': False,
                    'message': 'Only PUT and DELETE methods allowed'
                }

        return JsonResponse(response, status = response_status)

    except Exception as e:
        print("Erorrrrrrrrrrrrr", str(e))
        return JsonResponse({
                'status': False,
                'message': 'An error has occurred, please contact the administrator.'
            }, status = 500)

def prueba(request):
    return JsonResponse({'Hola':'Hola'})