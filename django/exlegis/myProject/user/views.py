from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    users = User.objects.all()
    serializer_class = UserSerializer
