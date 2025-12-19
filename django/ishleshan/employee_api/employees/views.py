from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from .permissions import IsAdmin, IsAdminorSelf

# Create your views here.

# --- Department CRUD (Admin only)
class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdmin]

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdmin]

# --- Employee CRUD (Role-based)
class  EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdmin]

class EmployeetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminorSelf]

# --- Custom ORM Query API
@api_view(['GET'])
@permission_classes(permissions.IsAuthenticated)
def employee_by_department(request,dept_id):
    employees = Employee.objects.filter(department_id=dept_id)
    serializer = EmployeeSerializer(employees, many=True)
    return serializer.data



