from django.urls import resolve
from movie.models import Movie
from django.http import JsonResponse

class MovieExists():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if resolve(request.path_info).url_name == 'movie':
            movie_id = resolve(request.path_info).kwargs.get('movie_id')
            try:
                movie = Movie.objects.get(id=movie_id)
                request.movie = movie
                return self.get_response(request)
            except:
                return JsonResponse({
                    'status': False,
                    'message': 'The movie with the id provided doesn\'t extist'
                }, status = 404)
