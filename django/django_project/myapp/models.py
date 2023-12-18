from django.db import models

# Create your models here.

class myUserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class myCandidate(models.Model):
    user_id = models.ForeignKey(myUserMaster, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50, default='none')
    state = models.CharField(max_length=50, default='none')
    city = models.CharField(max_length=50, default='none')
    address = models.CharField(max_length=150, default='none')
    dob = models.CharField(max_length=50, default='none')
    firstname = models.CharField(max_length=50, default='none')
    lastname = models.CharField(max_length=50, default='none')
    gender = models.CharField(max_length=50, default='none')
    job_title = models.CharField(max_length=50, default='none')
    job_type = models.CharField(max_length=50, default='none')
    job_category = models.CharField(max_length=50, default='none')
    country = models.CharField(max_length=50, default='none')
    year_of_exp = models.CharField(max_length=50, default='none')
    edu_level = models.CharField(max_length=50, default='none')
    website = models.CharField(max_length=50, default='none')
    min_salary = models.BigIntegerField( default=000000)
    max_salary = models.BigIntegerField( default=000000)
    job_desc = models.CharField(max_length=500, default='none')
    shift = models.CharField(max_length=50, default='none')
    profile_pic = models.ImageField(upload_to="app/img/myCandidate", default='none')

class myCompany(models.Model):
    user_id = models.ForeignKey(myUserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    myCompany_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo_pic = models.ImageField(upload_to="app/img/myCompany")
