# dashboard/urls/__init__.py
from ..views import home
from django.urls import path, include

urlpatterns = [
    path('',home, name='home'),
    path('students/', include('dashboard.urls.students')),  # Correctly include the students URLs
    path('courses/', include('dashboard.urls.courses')),  # Correctly include the students URLs
]
