from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.users, name='users'),
    path('<int:user_id>', views.user, name='user'),
]