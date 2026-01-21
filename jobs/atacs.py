# Duck Typing Example

class Book:
    def read(self):
        return "Reading a book..."

class Laptop:
    def read(self):
        return "Reading a PDF on laptop..."

def start_reading(obj):
    print(obj.read())

b = Book()
l = Laptop()

start_reading(b)   # Works
start_reading(l)   # Works
