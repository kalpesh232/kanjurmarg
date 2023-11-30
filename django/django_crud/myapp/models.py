from django.db import models

# Create your models here.
class Teacher(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=25)
    contact = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.Firstname
    
class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=25)
    Contact = models.BigIntegerField()

    def __str__(self) -> str:
        return self.Firstname
