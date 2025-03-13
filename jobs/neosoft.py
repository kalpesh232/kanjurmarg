# ######################################## Abstraction 

# from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def fun(self):
#         pass

# class B(A):
#     def __init__(self, value1):
#         self.v1 = value1

#     def fun(self):
#         return self.v1 ** 3
    
# class C(B):
#     def __init__(self, value1, value2, value3):
#         super().__init__(value1)
#         self.v2 = value2
#         self.v3 = value3

#     def fun(self):
#         cube = super().fun()
#         rectangle = self.v2 * self.v3
#         return f"Area of rectangle: {rectangle}, Volume of cube: {cube}"
    
# try:
#     a = A()  # This will raise an error
# except Exception as e:
#     print('Error:', e)

# b = C(3, 10, 20)
# print('Result:', b.fun())


# ############################################### Encapsulation 

# class BankAccount:
#     def __init__(self, account_holder, initial_balance, account_number):
#         self.account_number = account_number       # Public member
#         self._account_holder = account_holder      # Protected member
#         self.__balance = initial_balance           # Private member

#     # Public method to deposit
#     def deposit(self, amount):
#         self.__balance += amount

#     # Public method to withdraw
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds!")

#     # Getter for private balance
#     def get_balance(self):
#         return self.__balance

#     # Getter for protected account holder
#     def get_account_holder(self):
#         return self._account_holder

# # Creating an instance
# account = BankAccount("John Doe", 1000, "1234567890")

# # Accessing Public, Protected, and Private Members
# print("Account Number (Public):", account.account_number)  # Public member
# print("Account Holder (Protected):", account.get_account_holder())  # Protected via getter
# print("Balance (Private):", account.get_balance())  # Private via getter

# # Depositing and Withdrawing Money
# account.deposit(500)
# print("Balance after deposit:", account.get_balance())

# account.withdraw(200)
# print("Balance after withdrawal:", account.get_balance())

# account.withdraw(10000)  # Insufficient funds!
# print('----------')
# # Direct Access to Members
# print("Direct Public Access:", account.account_number)          # ✅ Works
# print("Direct Protected Access:", account._account_holder)      # ⚠️ Works, but not recommended
# try:
#     print("Direct Private Access:", account.__balance)          # ❌ Will raise an error
# except Exception as e:
#     print('Error:', e)



# ####################################### Function Overloading:

# class Add:
#     def sum(self, a,b):
#         print(a+b)

#     def sum(self, a,b,c):
#         print(a+b+c)

# a = Add()

# a.sum(56,56,56)

# class Add:
#     def sum(self, *args):
#         print(sum(args))

# a = Add()
# a.sum(10,20)
# a.sum(10,20,30)


# ######################## Method Overriding

# class Animal:
#     def make_sound(self):
#         print("Generic animal sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof! Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# # Create instances
# generic_animal = Animal()
# # my_dog = Dog()
# my_cat = Cat()

# # Call the overridden method
# # generic_animal.make_sound()  # Output: Generic animal sound
# # my_dog.make_sound()         # Output: Woof! Woof!
# my_cat.make_sound()         # Output: Meow!

# ➡️ Same method name + redefined in child + called via child object = Method Overriding. ✅

################################################  Handle Exceptions

# a = 5
# b = 8
# x = 10

# try:
#     print(a/b)
#     c = int(input('Enter Value : '))
#     print(c)
#     for i in range(x):
#         print(i)
#     print('No Error Occured')
# except ValueError as v :
#     print('ValueError Error Occured')
#     print('ValueError : ', v )
# except ZeroDivisionError as e :
#     print('ZeroDivisionError Error Occured')
#     print('ZeroDivisionError : ', e )
# except Exception as r :
#     print('Error Occured')
#     print('Error : ', r )
# finally:
#     print('Resource Closed')

# Define the user-defined exception outside the loop
# class MyException(Exception):
#     pass

# while True:
#     try:
#         c = int(input('Enter number: '))
#         if c < 15:
#             raise MyException('User not allowed')
#         else:
#             print('User allowed')
#             # break  # Exit the loop if input is valid
#     except MyException as e:
#         print(e)  # Print the custom error message
#     except ValueError:
#         print("Please enter a valid number.")  # Handle non-integer input


# ###################### with in pyhton 

# with open('neosoft.txt', 'r') as file:
#     print(file.read())

# ############################### Logging
# from flask import Flask
# import logging
# app = Flask(__name__)
# logging.basicConfig(filename='neosoft.log', level=logging.CRITICAL)
# @app.route('/')
# def index():
    # app.logger.debug('This is a debug message')
    # app.logger.info('This is an info message')
    # app.logger.warning('This is a warning message')
    # app.logger.error('This is an error message')
    # app.logger.critical('This is a critical message')
#     return 'Hello World !!'
# if '__main__' == __name__:
#     app.run(host='0.0.0.0', debug=True)

# ########################## Immutable String

# my_string = "Hello"
# print('ID 1 :', id(my_string))
# # Attempting to change a character at a specific index will result in an error
# # For example, the following line will raise an error: TypeError: 'str' object does not support item assignment
# # my_string[0] = 'h'

# # Instead, create a new string with the desired modifications
# my_string = my_string + " World"
# print('ID 2 :', id(my_string))
# print(my_string)  # Output: Hello World

# ######################## Multiple Decorators

# def div(a,b):
#     print('in div')
#     print(a/b)

# def swapping(fuc):
#     def wrapper1(a,b):
#         if a < b :
#             a,b = b ,a
#         return fuc(a,b)
#     return wrapper1
    
# def multiple(fuc):
#     def wrapper(a,b):
#         a *= 5
#         b *= 5
#         return fuc(a,b)
#     return wrapper

# div = swapping(div)
# if div.__name__ == 'wrapper1':
#     div = multiple(div)
# div(2,4)

# ############################### Flask Blueprint

# from flask import Flask
# from neosoft_blueprint import neosoft_blueprint

# app = Flask(__name__)
# app.register_blueprint(neosoft_blueprint)

# @app.route('/')
# def index():
#     return "This is an example app"


# if __name__ == '__main__':
#     app.run(debug=True)

# ############################# session.commit AND session.flush

# from sqlalchemy import create_engine, Column, Integer, String, Sequence
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()
# engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/alchemy',echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))

# Base.metadata.create_all(engine)

# # Adding a new user to the session
# stu1 = User(id =1, name='kalpesh')
# session.add(stu1)
# # Using flush to synchronize changes (check availability)
# session.flush()
# # At this point, the changes are in the session and synchronized with the database,
# # but they are not committed yet.

# # Now, let's modify the user's name before committing
# stu1.name = 'John Smith'
# # Using commit to make changes permanent
# session.commit()
# # The changes are now permanent in the database.

# # Let's query the database to verify the changes
# queried_user = session.query(User).filter_by(name='John Smith').first()
# print(queried_user.name)  # Output: John Smith

# #############  Global Interpreter Lock (GIL)

# import threading
# import time

# def task(name):
#     print(f"Task {name} starting")
#     time.sleep(2)
#     print(f"Task {name} completed")

# # Create threads
# thread1 = threading.Thread(target=task, args=("A",))
# thread2 = threading.Thread(target=task, args=("B",))

# # Start threads
# thread1.start()
# thread2.start()

# # Wait for threads to complete
# thread1.join()
# thread2.join()

# print("Both tasks are done")


#  ##########################   Django, signals

# from django.dispatch import receiver
# # models.py
# from django.db import models
# from neosoft_signanls import object_saved

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)

# # Signal sent when an object is saved
# @receiver(models.signals.post_save, sender=MyModel)
# def send_object_saved_signal(sender, instance, **kwargs):
#     object_saved.send(sender=sender, instance=instance)

#  ########################## Generators over  for loop  

# mylist = ["apple", "banana", "cherry"]

# # For loop with list
# for fruit in mylist:
#     print(fruit)

# # Generator function
# def fruit_generator():
#     for fruit in ["apple", "banana", "cherry"]:
#         yield fruit

# # Using the generator
# for fruit in fruit_generator():
#     print(fruit)

# ####################### Synchronous  & Asynchronous 

# --------- Synchronous 

# import time

# def task1(a):
#     print(f'task {a} start')
#     time.sleep(1)
#     print(f'task {a} end')


# def task2(b):
#     print(f'task {b} start')
#     time.sleep(1)
#     print(f'task {b} end')


# # # Synchronous execution
# task1('A')
# task2('B')

# ---------- Asynchronous

# import asyncio

# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(1)  # Simulate a non-blocking operation
#     print("Task 1 completed")

# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(1)  # Simulate a non-blocking operation
#     print("Task 2 completed")

# async def main():
#     await asyncio.gather(task1(), task2())

# # Run the event loop with the main coroutine
# asyncio.run(main())

# ####################### "list" and "array"

# my_list = [1, 2, 3, "apple", "banana"]

# from array import array
# my_array = array('i', [1, 2, 3, 4, 5])  # 'i' represents integer type

# import numpy as np

# float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=float)
# print(float_array)  # Output: [1.1 2.2 3.3 4.4]

# string_array = np.array(["apple", "banana", "cherry"])
# print(string_array)  # Output: ['apple' 'banana' 'cherry']

# mixed_array = np.array([42, "hello", 3.14], dtype=object)
# print(mixed_array)

# ########## shallow copy and deep copy 

# import copy
# original = [[1, 2, 3], [4, 5, 6]]
# print('original 1 : ', original)
# d = copy.deepcopy(original)
# print('d 1 : ',d)
# d[0][1] = 9
# print('original 2 : ', original)
# print('d 2 : ',d)

# ############## create a dictionary using a list 

# abc = ['a', 'b', 'c']
# dictionary = {xyz: None for xyz in abc}
# print(dictionary)
# Output: {'a': None, 'b': None, 'c': None}


# ----- In Python, class methods and instance methods are called in different ways.
##### 1. Instance Method:
class MyClass:
    def instance_method(self):
        print("This is an instance method.")

obj = MyClass()
obj.instance_method()  

##### 2. Class Method:
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")

MyClass.class_method()  

# #####  Static Method  #####
class Demo:
    @staticmethod
    def static_method():
        print('Tish is Static Method  ')
Demo.static_method()

# Difference Between APIView and ViewSet in Django REST Framework (DRF)

# ------- APIView ---------
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleAPIView(APIView):
    def get(self, request):
        return Response({"message" : "Hello From APIView"})

# -------- ViewSet --------
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ExampleViewSet(ViewSet):
    def list(self, request):
        return Response({"massage" : "Hello From ViewSet"})
    
# #########
names = ["Kalpesh", "Shinde", "Address"]
ls = []
for i in names:
    ls.append(i[0])
x = '-'.join(map(str,ls))
print(x)



 





