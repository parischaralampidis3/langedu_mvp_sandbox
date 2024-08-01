from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, students, create_student, StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),  # Note the trailing slash
    path('create_student/', create_student, name='create_student'),  # Note the trailing slash
    path('', include(router.urls))
]
