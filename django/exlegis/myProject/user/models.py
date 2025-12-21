from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharFeild(max_len=100)
    email = models.EmailFields()

