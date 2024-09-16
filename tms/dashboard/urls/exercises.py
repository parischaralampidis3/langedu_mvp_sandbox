from django.urls import path
from ..views import exercises,select_exercise,create_exercise_container

urlpatterns = [
    path('exercises', exercises, name='exercises'),
    path('select_exercise', select_exercise, name='select_exercise'),
    path('create_exercise_container', create_exercise_container, name='create_exercise_container'),
]