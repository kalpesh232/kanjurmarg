from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_product, name='register'),
    path('products_list/', views.products_list, name='products_list'),
]
