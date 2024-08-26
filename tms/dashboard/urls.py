
from django.urls import path


from .views import home,courses,course,create_course ,students, student, create_student, update_student, delete_student, StudentListView, StudentDetailView

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('student/<int:id>', student, name='student'),
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:id>', update_student, name='update_student'),
    path('course/<int:id>/', course, name='course'),
    path('create_course/', create_course, name='create_course'),
    path('enroll_student/', enroll_student, name='enroll_student'),
]

