# -------------- Fibonacci 

result = 0

def fib(n):
    a =0
    b =1
    for i in range(3, n+2):
        c = a + b
        a,b = b,c
        print('c :',c)
n = 50
fib(n)

