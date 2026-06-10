from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Middleware Demo!")

def register_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Product.objects.create(name=name, price=price)
        return render(request, 'register_product.html', {"success" : True})
    return render(request, 'register_product.html')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {"myProducts" : products})
