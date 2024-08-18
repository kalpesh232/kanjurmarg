from django.shortcuts import render
from .serializers import SingerSerializers, SongSerializers
from rest_framework import viewsets
from .models import Song, Singer

# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializers