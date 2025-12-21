from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    ROLE_CHOICES = (
        ('ADMIN' , 'Admin'),
       ( 'EMPLOYEE' , 'Employee')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    departname = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designtion = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date  = models.DateField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Employee')
    status = models.CharField(max_length=10, default='Employee')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
