
from django.contrib import admin
from django.urls import path
from .views import (
    EmployeeListCreate, EmployeetDetail, DepartmentDetail, DepartmentListCreate,employee_by_department
)

urlpatterns = [
     # Employee CRUD
     path('employees/', EmployeeListCreate.as_view()),
     path('employees/<int:pk>/', EmployeetDetail.as_view()),

     # Department CRUD
     path('departments/', DepartmentListCreate.as_view()),
     path('departments/<int:pk>', DepartmentDetail.as_view()),

      # ORM query
      path('employees/epartment/<int:dept_id>', employee_by_department)
]