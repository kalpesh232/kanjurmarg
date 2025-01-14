# flat_ls = []
# def flatten_list(data):
#     for item in data:
#         if isinstance(item,list):
#             # flat_ls.extend(flatten_list(item))
#             flatten_list(item)
#         else:
#             flat_ls.append(item)

# data =  [1, 2, 3, [4, 5, [6, 7, 8, [13, 14]], 9, 10], 11, 12]
# flatten_list(data)
# print(flat_ls)

import numpy as np

# Sample sensor data (temperature and humidity readings)
temperature = np.array([25.5, 26.1, 25.8, 26.0, 25.9])
humidity = np.array([60.2, 59.8, 60.5, 60.1, 59.9])

# Calculate real-time statistics
avg_temp = np.mean(temperature)  # Average temperature
min_temp = np.min(temperature)   # Minimum temperature
max_temp = np.max(temperature)   # Maximum temperature

avg_humidity = np.mean(humidity)  # Average humidity
min_humidity = np.min(humidity)   # Minimum humidity
max_humidity = np.max(humidity)   # Maximum humidity

print(f"Temperature -> Avg: {avg_temp}, Min: {min_temp}, Max: {max_temp}")
print(f"Humidity -> Avg: {avg_humidity}, Min: {min_humidity}, Max: {max_humidity}")


# ------------- X -------------
# myls = []
# counter = 1
# def sum_of_nested_list(data):
#     global counter
#     for i in data:
#         if isinstance(i, list):
#             counter += 1
#             sum_of_nested_list(i)
#         else:
#             myls.append(i)
#     return myls
# data = [1, [2, [3, 4], 5], 6]
# result =  sum_of_nested_list(data)
# print('result : ', result)
# print('sum of nested list : ', sum(result))
# print('Depth of Nested List : ', counter)
# even_ls = [i for i in result if i %2 == 0 ]
# print('even nested list : ', even_ls)

# def reverse_of_nested_list(data):
#     print('1')
#     myls = []
#     print('2')
#     for i in reversed(data):
#         print('3')
#         if isinstance(i, list):
#             print('4')
#             reversed_sublist = reverse_of_nested_list(i) 
#             print('5', reversed_sublist)
#             myls.append(reversed_sublist) 
#             print('6')
#         else:
#             print('7')
#             myls.append(i)
#             print('8',i)
#     print('9')
#     print('-----')
#     return myls
# data = [1, [2, [3, 4], 5], 6]
# result =  reverse_of_nested_list(data)
# print('data : ', data)
# print('result : ', result)

# car = []
# def Cartesian(data):
#     for i in data[0]:
#         for j in data[1]:
#             car.append([i] + [j])
#     return car
# data = [[1, 2], [3, 4]]
# result = Cartesian(data)
# print('result : ', result)

# mydict = {}
# def Flatten(data, main_key=''):
#     for key, value in data.items():
#         if main_key != '' :
#             new_key =  main_key + '.' + key
#         else:
#             new_key = key
#         if isinstance(value, dict):
#             Flatten(value,new_key)
#         else:
#             mydict[new_key] = value
#     return mydict

# data = {'a': 1, 'b': {'c': 2, 'd': {'e': 3,'f': 4}}}
# result = Flatten(data)
# print('result : ', result)

# def fib(num):
#     a , b = 0,1
#     if num < 0:
#         print("Invalid input: Fibonacci sequence is not defined for negative numbers.")
#         return
#     elif  num == 0:
#         c = 0
#     elif num == 1 :
#          c = 1
#     else:
#         for _ in range(2,num+1):
#             c = a+b
#             a ,b = b,c
#     print(c)
# num = int(input('Enter Number : '))
# fib(num)


# prime_ls = []
# num = 0
# while True:
#     if num == 0 or num == 1:
#         pass
#     elif num == 2 :
#         prime_ls.append(num)
#     else:
#         for i in range(2, num):
#             if num %  i == 0 :
#                 # print(f'{num} is not a prime number')
#                 break
#         else:
#             print(f'{num} is  a prime number')
#             prime_ls.append(num)
#     num += 1
#     if len(prime_ls) == 50 :
#         print(prime_ls)
#         sum_ls = sum(prime_ls)
#         print('sum of list : ', sum_ls)
#         break

# num = int(input('enter number : '))
# stor = num
# temp = 0
# while num > 0 :
#     last_digit = num % 10
#     mul_10 = (temp * 10) 
#     temp =  mul_10 + last_digit
#     num //= 10
# if temp == stor:
#     print(f'{stor} is palindroman')
# else:
#     print(f'{stor} is not palindroman')

# from functools import reduce
# ls = [9,7,6,9,9,7,3,7,6,6]
# x = reduce( lambda x,y : x+y,  ls )
# print(x)

# x = lambda x,y : x+y 
# print(x(10,20))

mychar = 'kalpeshharishchandrashinde'
ls1 = []
str1 = ''
for i in mychar:
    if i not in str1:
        str1 += i
    else:
        ls1.append(str1)
        str1 = i
ls1.append(str1)
dict1 = {j : len(j) for j in ls1}
result = {k : v for k,v in dict1.items() if v == (max(dict1.values()))}
print(result)

