from django.urls import resolve
from movie.models import Movie, Rating
from django.http import JsonResponse

class MovieExists():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if resolve(request.path_info).url_name in ['movie', 'create_rating']:
            movie_id = resolve(request.path_info).kwargs.get('movie_id')
            try:
                movie = Movie.objects.select_related().get(id=movie_id)
                request.movie = movie
                return self.get_response(request)
            except:
                return JsonResponse({
                    'status': False,
                    'message': 'The movie with the id provided doesn\'t extist'
                }, status = 404)
        else:
            return self.get_response(request)

class RatingExists():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if resolve(request.path_info).url_name == 'rating':
            rating_id = resolve(request.path_info).kwargs.get('rating_id')
            try:
                rating = Rating.objects.get(id=rating_id)
                request.rating = rating
                return self.get_response(request)
            except:
                return JsonResponse({
                    'status': False,
                    'message': 'The rating with the id provided doesn\'t extist'
                }, status = 404)
        else:
            return self.get_response(request)