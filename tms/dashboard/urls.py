from django.http import HttpResponse
from django.urls import path
from .views import home
urlpatterns = [
    path('', home, name='home'),
]
