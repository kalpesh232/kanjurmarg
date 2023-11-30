from django.urls import path, include
from . import views

urlpatterns = [
  path("",views.html_form,name='html_form'),
  path("home", views.Index, name='all_posts')
]