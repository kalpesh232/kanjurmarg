from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.showPosts, name='showposts'),
   path("likepost", views.likedPost, name='likepost')
]