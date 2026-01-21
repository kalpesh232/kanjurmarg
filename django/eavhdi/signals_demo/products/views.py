from django.shortcuts import render, redirect
from .forms import ProductForm
from django.http import HttpResponse
from .models import Product

# Create your views here.

def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print('yes form is valid')
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'register_product.html', {'form':form})


def success(request):
    return HttpResponse("Product Registered Successfully!")

def product_list(request):
    myProducts = Product.objects.all()
    print('myProducts : ', myProducts)
    return render(request, 'product_list.html', {'myProducts':myProducts})




