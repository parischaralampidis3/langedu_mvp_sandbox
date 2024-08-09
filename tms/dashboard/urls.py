from django.urls import path, include
from .views import home, students, create_student, StudentListView, StudentDetailView

urlpatterns = [
    path('', home, name='home'),
    path('studentsApi/', StudentListView.as_view(), name="student-list"),
    path('studentApi/<int:id>/', StudentDetailView.as_view(), name="student-detail"),
    path('students/', students, name='students'),
    path('create_student/', create_student, name='create_student'),
]
