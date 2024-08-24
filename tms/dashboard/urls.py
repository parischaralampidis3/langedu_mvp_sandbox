
from django.urls import path

from .views import home,courses,course,create_course ,students, student, create_student, update_student, delete_student, StudentListView, StudentDetailView

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('student/<int:id>', student, name='student'),
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:id>', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),

    path('studentsApi/', StudentListView.as_view(), name="student-list"),
    path('studentsApi/<pk>', StudentDetailView.as_view(), name="student-detail"),

    path('courses/', courses, name='courses'),
    path('course/<int:id>', course, name='course'),
    path('create_course/', create_course, name='create_course')

]