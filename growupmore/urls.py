# growupmore/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authuser.urls')),  # Prefix with 'auth/' for clarity
]
