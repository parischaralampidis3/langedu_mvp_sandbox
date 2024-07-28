
from django.urls import path
from .views import home
from .views import students
from .views import create_student
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('create_student/', create_student, name='create_student'),
]
