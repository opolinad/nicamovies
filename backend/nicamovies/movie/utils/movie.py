from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from django.http import JsonResponse
from movie.models import Movie
from movie.models import Rating

def get_movies(page_number, per_page=10):
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

def get_movie(movie:Movie)->JsonResponse:
    return {
        'status': True,
        'message': 'Movie obtained successfully',
        'movie': model_to_dict(movie)
    }

def update_movie(movie:Movie, title:str, release_date:str, genre:str, plot:str)->JsonResponse:
    Movie.objects.filter(id=movie.id).update(
        title=title,
        release_date=release_date,
        genre=genre,
        plot=plot
    )
    movie.refresh_from_db()

    return {
        'status': True,
        'message': 'Movie updated successfully',
        'movie': model_to_dict(movie)
    }

def delete_movie(movie:Movie)->JsonResponse:
    movie.delete()
    return {
        'status': True,
        'message': 'Movie deleted successfully',
    }

def create_rating_for(movie_id:int, user_id:int, rating:float, comment:str):
    rating = Rating.objects.create(
        rating=rating,
        comment=comment,
        movie_id=movie_id,
        user_id=user_id,
    )

    return {
        'status': True,
        'message': 'Rating created successfully',
        'movie': model_to_dict(rating)
    }

def update_rating(rating:Rating, rating_given:float, comment:str):
    Rating.objects.filter(id=rating.id).update(
        rating=rating_given,
        comment=comment,
    )
    rating.refresh_from_db()

    return {
        'status': True,
        'message': 'Rating updated successfully',
        'movie': model_to_dict(rating)
    }

def delete_rating(rating:Rating):
    rating.delete()

    return {
        'status': True,
        'message': 'Rating deleted successfully',
    }