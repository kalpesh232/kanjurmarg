from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.resigster_product, name='resigster_product'),
    path('products/',views.products_list, name='products_list'),
]