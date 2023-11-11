from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def html_form(request):
    return render(request, 'html_form.html')

def Index(request):
    posts = Post.objects.all()
    print('posts : ',posts)
    return render(request, 'ajax_app/index.html',{'posts' : posts})
