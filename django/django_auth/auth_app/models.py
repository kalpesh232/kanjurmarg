from django.db import models

# Create your models here.
class UserRegister(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)
    Password = models.CharField(max_length=50)
    ImageName = models.CharField(max_length=25, default='0000000')
    pic = models.ImageField(upload_to='auth_app/static/img/')
