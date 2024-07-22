
from django.urls import path
from .views import home
from .views import users
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('users/', views.index_users, name='index_users')
]
