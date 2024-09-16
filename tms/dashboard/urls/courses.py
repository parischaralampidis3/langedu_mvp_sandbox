from django.urls import path
from ..views import courses, course,create_course,update_course,delete_course,enroll_lesson

urlpatterns = [
    path('courses', courses, name='courses'),
    path('<int:id>/', course, name='course'),
    path('create_course', create_course, name='create_course'),
    path('update_course/<int:id>/', update_course, name='update_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),
    path('enroll_lesson', enroll_lesson, name='enroll_lesson')
]