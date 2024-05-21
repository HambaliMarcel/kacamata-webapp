from django.urls import path
from . import views

urlpatterns = [
    path('', views.materi_list, name='materi_list'),
    path('upload/', views.upload_materi, name='upload_materi'),
]
