from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view          #  function-based views (FBVs)
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['POST'])
def resigster_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Product registered successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message' : f'Product not registered {serializer.errors} '}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)
