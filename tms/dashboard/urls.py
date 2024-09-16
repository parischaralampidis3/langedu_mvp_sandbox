from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),  # App-specific URLs
    path('courses/', include('courses.urls')),  # App-specific URLs
    path('lessons/', include('lessons.urls')),  # App-specific URLs
]

