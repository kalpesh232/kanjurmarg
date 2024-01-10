# ######################################## Abstraction 

# from abc import ABC , abstractmethod

# class A(ABC):
#     @abstractmethod
#     def fun_a():
#         pass
# class B(A):
#     def __init__(self,radius):
#         self.radius = radius

#     def fun_a(self):
#         return 3.14 * self.radius * self.radius
    
# value = 5
# b = B(value)
# print(b.fun_a())

# ############################################### Encapsulation 

# class bankAccount:
#     def __init__(self, ac_holder_name, account_balance):
#         self._ac_holder_name = ac_holder_name
#         self.__account_balance = account_balance

#     def deposit(self, deposit_amt):
#         self.__account_balance += deposit_amt
#         return self.__account_balance
    
#     def withdrawal(self, withdrawal_amt):
#         if self.__account_balance > withdrawal_amt:
#             self.__account_balance -= withdrawal_amt
#             return self.__account_balance
#         return 'Account Balance Should be Breater then Witdrawal Balanace'
    
#     def acholderName(self):
#         return self._ac_holder_name
    
#     def acBalance(self):
#         return self.__account_balance
    
# ba = bankAccount('kalpesh shinde', 5000)
# print('Account Balance : ',  ba.acBalance())
# print('Account Balance after Deposit: ',  ba.deposit(500))
# print('Account Balance after Withdrawal: ',  ba.withdrawal(10000))
# print('Account Holder Name: ',  ba.acholderName())
# print('Account Final Balance: ',  ba.acBalance())
# print(ba._ac_holder_name)
# print(ba.__account_balance)

# ####################################### Function Overloading:

# class Add:
#     def sum(self, a,b):
#         print(a+b)

#     def sum(self,a,b,c):
#         print(a+b+c)

# a = Add()
# a.sum(56,56,56)
# pause.
# ######################## Method Overriding

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create instances
generic_animal = Animal()
# my_dog = Dog()
my_cat = Cat()

# Call the overridden method
# generic_animal.make_sound()  # Output: Generic animal sound
# my_dog.make_sound()         # Output: Woof! Woof!
my_cat.make_sound()         # Output: Meow!

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

# user define exception
# class MyException(Exception):
#     pass

# c = 25
# if c > 5 :
#     raise MyException("somrting went wrong")

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
#     app.logger.debug('This is a debug message')
    # app.logger.info('This is an info message')
#     app.logger.warning('This is a warning message')
#     app.logger.error('This is an error message')
#     app.logger.critical('This is a critical message')
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

# # Shared counter variable
# counter = 0

# # Function to calculate the square of numbers
# def calculate_square():
#     global counter
#     for _ in range(1_000_000):
#         counter += 1  # Increment the counter

# # Create two threads to perform the task
# thread1 = threading.Thread(target=calculate_square)
# thread2 = threading.Thread(target=calculate_square)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# # Print the final counter value
# print("Final Counter Value:", counter)

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

# def task1():
#     print("Task 1 completed")

# def task2():
#     print("Task 2 completed")

# # Synchronous execution
# task2()
# task1()

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





