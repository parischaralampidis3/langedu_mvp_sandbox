
from django.urls import path
from .views import home
from .views import users
urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
]
