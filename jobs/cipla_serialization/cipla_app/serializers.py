from .models import Singer, Song
from rest_framework import serializers

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title','singer','duration']

class SingerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name','gender']