from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.movies, name='movies'),
    path('<int:movie_id>', views.movie, name='movie'),
]