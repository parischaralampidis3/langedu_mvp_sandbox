
from django.urls import path, include

from .views import StudentListView, StudentDetailView, EnrollmentCourseListView, EnrollmentCoursesDetailView, home, students, student, create_student, update_student, enroll_student, delete_student, courses, course, create_course


urlpatterns = [
    path('', home, name='home'),
    path('coursesApi/', EnrollmentCourseListView.as_view(), name="courses-list"),
    path('coursesApi/<ind:id>', EnrollmentCoursesDetailView.as_view(), name="courses-detail"),
    path('studentsApi/', StudentListView.as_view(), name="student-list"),
    path('studentApi/<int:id>/', StudentDetailView.as_view(), name="student-detail"),
    path('students/', students, name='students'),  # List of students
    path('student/<int:id>/', student, name='student'),  # Student details with enrolled courses
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('courses/', courses, name='courses'),
    path('course/<int:id>/', course, name='course'),
    path('create_course/', create_course, name='create_course'),
    path('enroll_student/', enroll_student, name='enroll_student'),

]

