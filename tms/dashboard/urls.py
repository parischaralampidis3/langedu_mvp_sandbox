from django.urls import path
from .views import home, students, create_student, delete_student

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),  # Note the trailing slash
    path('create_student/', create_student, name='create_student'),  # Note the trailing slash
    path('delete_student/<int:id>/', delete_student, name='delete_student')
]
