from django.db import models

# Create your models here.

class Post(models.Model):
    post_heaading = models.CharField(max_length=200)

class myPost(models.Model):
    post_heaading = models.CharField(max_length=200)
    post_text = models.TextField()

class Like(models.Model):
    likedpost = models.ForeignKey(myPost,on_delete=models.CASCADE)
