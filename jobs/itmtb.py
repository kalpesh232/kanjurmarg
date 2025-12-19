### ✅ 1. **Profile the Code**

# import time 
# import cProfile

# def fast_function():
#     sum([i for i in range(1000)])

# def slow_function():
#     time.sleep(1)

# def main():
#     fast_function()
#     slow_function()

# # if __name__ == '__main__':
# #     main()

# cProfile.run("main()")

### ✅ 4. **Cache Results * lru_cache *

# import time
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def slow_square(n):
#     time.sleep(1)
#     return n * n

# print(slow_square(5))
# print(slow_square(5))

# from functools import lru_cache

# @lru_cache(None)
# def fib(n):
#     print("n : ", n)
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(40))   # fast, because cached

def fib(n):
    a,b = 0,1
    if n < 0:
        print("Incorrect input")
        
    # Check if n is equal to 0
    elif n == 0:
        return 0
      
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(n):
            a,b = b, a+b
        return a
print(fib(40))
