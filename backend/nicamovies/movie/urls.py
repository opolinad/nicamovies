from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.movies, name='movies'),
    path('<int:movie_id>', views.movie, name='movie'),
    path('<int:movie_id>/user/<int:user_id>/create-rating', views.create_rating, name='create_rating'),
    path('rating/<int:rating_id>', views.rating, name='rating')
]