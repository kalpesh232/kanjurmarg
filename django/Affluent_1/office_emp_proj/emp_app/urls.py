from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_emp', views.view_emp, name='view_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp_list'),  # URL for displaying employees
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),  # URL for deleting an employee
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('update_emp/<int:emp_id>/', views.update_emp, name='update_emp')
]