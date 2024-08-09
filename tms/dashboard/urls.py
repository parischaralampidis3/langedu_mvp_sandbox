
from django.urls import path
from .views import home, students, student, create_student, update_student, delete_student, StudentListView, StudentDetailView

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),  # Note the trailing slash
    path('student/<int:id>', student, name='student'),
    path('create_student/', create_student, name='create_student'),  # Note the trailing slash
    path('update_student/<int:id>', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student')
    path('studentsApi/', StudentListView.as_view(), name="student-list"),
    path('studentApi/<int:id>/', StudentDetailView.as_view(), name="student-detail")
]
