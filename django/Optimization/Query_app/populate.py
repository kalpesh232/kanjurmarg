from .models import Author, Book

def create_data():
    Author.objects.all()
    Book.objects.all()

    a1 = Author.objects.create(name="J.K. Rowling")
    a2 = Author.objects.create(name="George R. R. Martin")
    a3 = Author.objects.create(name="Stephen King")

    Book.objects.create(title="Harry Potter 1", author=a1)
    Book.objects.create(title="Harry Potter 2", author=a1)
    Book.objects.create(title="Game of Thrones", author=a2)
    Book.objects.create(title="The Shining", author=a3)
    Book.objects.create(title="IT", author=a3)

    print("Dummy data created!")
