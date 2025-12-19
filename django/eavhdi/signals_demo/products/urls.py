from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_product, name='register_product'),
    path('product_list/', views.product_list, name='product_list')
]