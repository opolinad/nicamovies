from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from movie.models import Movie

def get_movie(page_number, per_page=10):
    movies = Movie.objects.get_queryset().order_by('id').values()
    paginator = Paginator(movies, per_page)
    page_obj = paginator.get_page(page_number)
    try:
        movies_list = list(paginator.page(page_number))
    except:
        if page_number>1:
            movies_list = list(paginator.page(page_number-1))
        else:
            movies_list = []

    return {
        'movies':movies_list,
        'count': paginator.count,
        'num_pages':paginator.num_pages
    }

def create_movie(title, release_date, genre, plot):
    movie = Movie.objects.create(
        title=title,
        release_date=release_date,
        genre=genre,
        plot=plot
    )
    return {
        'status': True,
        'message': 'Movie created successfully',
        'movie': model_to_dict(movie)
    }