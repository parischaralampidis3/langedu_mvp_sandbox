
from django.urls import path
from .views import home
from .views import users
from .views import create_user
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('create_user/', create_user, name='create_user'),
]
