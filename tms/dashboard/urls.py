from django.urls import path
from .views import home, students, student, create_student, update_student, delete_student, courses

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),  # Note the trailing slash
    path('student/<int:id>', student, name='student'),
    path('create_student/', create_student, name='create_student'),  # Note the trailing slash
    path('update_student/<int:id>', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('courses/', courses, name = 'courses')
]
