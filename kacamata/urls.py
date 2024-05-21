from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('materi.urls')),
]


# App URLs: Create materi/urls.py and define the URL patterns.
