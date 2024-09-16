from django.urls import path
from ..views import students, student,create_student,update_student,delete_student,enroll_student

urlpatterns = [
    path('students', students, name='students'),
    path('<int:id>/', student, name='student'),
    path('create_student', create_student, name='create_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('enroll_student', enroll_student, name='enroll_student')
]