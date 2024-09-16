# dashboard/urls/__init__.py
from ..views import home
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('students/', include('dashboard.urls.students')),
    path('courses/', include('dashboard.urls.courses')),
    path('lessons', include('dashboard.urls.lessons'))
]
