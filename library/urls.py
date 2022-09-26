from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('media/', views.media, name='media'),
    path('blog/', views.blog(), name='blog'),
]

