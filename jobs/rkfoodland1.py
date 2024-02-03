# ########################## Explain MVC in Django 

# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=120)
#     author = models .CharField(max_length=50)
#     pub_date = models.DateField()

# from django.shortcuts import render
# # from .models import Book

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books' : books})

#  ############# class base view and function base view in Django

# from django.shortcuts import render
# from django.http import HttpResponse

# def my_view(request):
#     return render(request, 'my_template.html')

# from django.shortcuts import render
# from django.views import View

# class Myview(View):
#     def my_view(self, request):
#         return render(request, 'my_template.html')

#  ######################  polymorphism in Python 

# Base class representing a shape
class Shape:
    def calculate_area(self):
        pass

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Function that works with objects of different shapes
def print_area(shape):
    print(f"Area: {shape.calculate_area()}")

# Create instances of different shapes
rectangle = Rectangle(width=5, height=10)
circle = Circle(radius=7)

# Use the function with different shape objects
print_area(rectangle)  # Output: Area: 50
print_area(circle)     # Output: Area: 153.86



