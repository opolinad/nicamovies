from django.http import HttpResponse, JsonResponse, request
from .utils.movie import get_movie, create_movie
from .validators.movie import is_create_movie_info_valid

def movies(request:request)->JsonResponse:
    try:
        if request.method == 'GET':
            page_number = request.GET.get('page_number', 1)
            per_page = request.GET.get('per_page', 10)
            movies = get_movie(page_number, per_page)

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
            else:
                response = {
                    'status': False,
                    'message': valid_request[1]
                }

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({
                'status': False,
                'message': 'An error has occurred, please contact the administrator.'
            })

