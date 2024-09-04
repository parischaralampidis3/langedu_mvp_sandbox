from django.urls import path
from .views import home, students, student, create_student, update_student, enroll_student, delete_student, courses, \
    course, create_course, lessons, create_lesson
urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),  # List of students
    path('student/<int:id>/', student, name='student'),  # Student details with enrolled courses
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('courses/', courses, name='courses'),
    path('course/<int:id>/', course, name='course'),
    path('create_course/', create_course, name='create_course'),
    path('lessons/', lessons, name='lessons'),
    path('create_lesson/', create_lesson, name='create_lesson'),
    path('enroll_student/', enroll_student, name='enroll_student'),
]

