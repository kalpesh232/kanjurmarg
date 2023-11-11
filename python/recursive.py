# how i got x2 :  3
def factorial(x):
    if x == 1:
        return x
    else:
        a = x * factorial(x-1)
        return (a) 
# x = int(input('Int : '))
# result = factorial(x)
# print(f'Factorial of {x} is {result}')  


# labmda
x = lambda a,b : a*b 
print('x : ',x(10,50))

x = 1
def fib(n):
    global x
    for i in range(1,n+1):
        x *= i
    print('x : ', x)
fib(5)

# import random

# print(random.randrange(100000, 999999))
# print(random.randint(10))

import math  

#Remove - sign of given number
print(math.fabs(-66.43))  # always return a floating-point number
print(math.fabs(-7))
x = abs(-7)
print(x)

x = 45.25458
# print(round(x,1))

