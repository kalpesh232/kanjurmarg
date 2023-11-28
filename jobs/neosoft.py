# ######################################## Abstraction 

# from abc import ABC , abstractmethod
# class A(ABC):
#     @classmethod
#     def fun_a():
#         pass
# class B(A):
#     def __init__(self, radius):
#         self.radius = radius

#     def fun_a(self):
#         return 3.14 * self.radius * self.radius

# value = 5
# a = B(value)
# print(a.fun_a())


# ############################################### Encapsulation 

# class BankAccount:
#     def __init__(self, account_holder, initial_balance):
#         self._account_holder = account_holder  # Protected member
#         self.__balance = initial_balance  # Private member

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds!")

#     def get_balance(self):
#         return self.__balance

#     def get_account_holder(self):
#         return self._account_holder


# # Creating an instance of BankAccount
# account = BankAccount("John Doe", 1000)

# # Accessing protected and private members
# print("Account Holder:", account.get_account_holder())  # Protected member
# print("Balance:", account.get_balance())  # Private member

# # Depositing and withdrawing money
# account.deposit(500)
# print("Balance after deposit:", account.get_balance())

# account.withdraw(200)
# print("Balance after withdrawal:", account.get_balance())

# account.withdraw(10000)  # Insufficient funds!

# # Trying to access private member directly (will result in an error)
# # print(account.__balance)

# ####################################### Function Overloading:

# class Add:
#     def sum(self, a,b):
#         print(a+b)

#     def sum(self, a,b,c):
#         print(a+b+c)

# a = Add()
# a.sum(89,45,12)

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

# 

a = 5
b = 8
x = 10

try:
    print(a/b)
    c = int(input('Enter Value : '))
    print(c)
    for i in range(x):
        print(i)
    print('No Error Occured')
except ValueError as v :
    print('ValueError Error Occured')
    print('ValueError : ', v )
except ZeroDivisionError as e :
    print('ZeroDivisionError Error Occured')
    print('ZeroDivisionError : ', e )
except Exception as r :
    print('Error Occured')
    print('Error : ', r )
finally:
    print('Resource Closed')

# # user define exception
# class MyException(Exception):
#     pass

# c = 25
# if c > 5 :
#     raise MyException("somrting went wrong")
