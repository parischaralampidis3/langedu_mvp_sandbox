from django.urls import path
from ..views import lessons, lesson, create_lesson,update_lesson,enroll_question_to_lesson,delete_lesson

urlpatterns = [
    path('lessons', lessons, name='lessons'),
    path('<int:id>/', lesson, name='lesson'),
    path('create_lesson', create_lesson, name='create_lesson'),
    path('<int:id>/', update_lesson, name='update_lesson'),
    path('<int:id>/', delete_lesson, name='delete_lesson'),
    path('enroll_lesson',enroll_question_to_lesson, name='enroll_question_to_lesson')
]