from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('media/', views.media, name='media'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]

