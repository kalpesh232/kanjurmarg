from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def showPosts(request):
    posts = myPost.objects.all()
    print('all_post : ', posts)
    return render(request, 'ajax_app0/posts.html', {'posts' : posts})

def likedPost(request):
    print('00000000000')
    if request.method == "GET":
        post_id = request.GET['post_id']
        likedpost = myPost.objects.get(pk=post_id)
        l = Like(post = likedPost)
        l.save()
        return HttpResponse('success !')
    else:
        return HttpResponse('Method is not GET')
