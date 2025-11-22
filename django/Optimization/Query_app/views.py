from django.shortcuts import render
from .models import Book, Author
from rest_framework import viewsets
from django.http import JsonResponse
from django.db import connection

# Create your views here.

def test_select(request):
    books = Book.objects.select_related("author")

    data = []
    for b in books:
        data.append({
            "book" : b.title,
            "author" : b.author.name
        })

    print(connection.queries)
    return JsonResponse(data, safe=False)

def test_prefetch(request):
    authors = Author.objects.prefetch_related("books")

    data = []
    for a in authors:
        print('aaaaaaa : ', a)
        data.append({
            "auther" : a.name,
            "book" : [b.title for b in a.books.all()]
        })

    print(connection.queries)  # show SQL
    return JsonResponse(data, safe=False)
