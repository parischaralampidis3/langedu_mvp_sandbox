from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
    path('lessons/', include('lessons.urls')),
    path('exercises/', include('exercises.urls')),
    path('questions/', include('questions.urls')),
]

