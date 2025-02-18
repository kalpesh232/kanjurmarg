# ---------- request-response cycle
# from flask import Flask
# app = Flask(__name__)
# app.route('/')
# def index():
#     return "Hello!"

# from django.http import HttpResponse
# def index(request):
#     return(HttpResponse, "Hello!")

# ----------  Structuring a **REST API** in **Flask** or **Django**

'''
- **Flask** 
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app) 

class HelloWorld(Resource):
    def get(self):
        return jsonify(message="Hello, World!") 

api.add_resource(HelloWorld, '/api/hello')

if __name__ == '__main__':
    app.run(debug=True)

## **In Django**:

   - In `models.py`:
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

   - In `serializers.py`:
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

   - In `views.py`:
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
     
   - In `urls.py`:
from django.urls import path
from .views import *

urlpatterns = [
    path('api/items/', views.ItemList.as_view(), name='item-list'),
]
'''