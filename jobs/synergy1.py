# ----- modify string 
# x = "kalpesh"
# x1 = list(x)
# x1[3] = 'x'
# y = str(x1)
# print("".join(x1))

# ----------    Write a Python program to check if a string is a palindrome.

# x = "shinde"
# x1 = list(x)
# x2 = x1[::-1]
# if x1 == x2 :
#     print('x1 and x2 are palindrom')
# else:
#     print('x1 and x2 are not palindrom')

# print(x1)
# print(x2)


# ------------ Write a Python program to find the factorial of a number.

# def fact(n):
#     if n < 2 :
#         return n
#     else :
#         return fact(n-1) * n
# x = fact(8)
# print(x)

# ---------- Write a Python program to find the largest element in a list.

# temp = 0
# x = [78,21,59,63,47,25,95,4,10]
# x2 = max(x)
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i] > x[j]:
#             temp = x[i]
#             x[i] = x[j]
#             x[j] = temp
# print(x[0])

#  ---------- Write a Python program to reverse a string.

# x = 'kalpesh'
# x1 = list(x)
# x2 = x1[::-1]
# print(''.join(x2))

# ----------  Write a Python program to count the frequency of each element in a list.

# x = [8,0,0,7,2,8,9,7,7,6]
# x1 = {}
# for i in x:
#    x1[i] = 0
# x2 = list(x1.keys())
# count = 0
# for i in range(len(x2)):
#     for j in range(len(x)):
#         if x2[i] == x[j] :
#             count += 1
#         x1[x2[i]] = count
#     count = 0
# print('frequency_count 1 : ', x1)

# --------- Write a Python program to check if a number is prime.

# def is_prime(x):
#     if x < 2:
#         print(f'{x} is not a Prime Number')
#     for i in range(2, x):
#         if x % i == 0 :
#             print(f'{x} is Not  a Prime Number')
#             break
#     else:
#         print(f'{x} is  a Prime Number')
        

# x = int(input('Enter Number : '))
# is_prime(x)

# --------- Write a Python program to find the common elements between two lists.

# x = [1, 2, 3, 4, 5]
# y = [4, 5, 6, 7, 8,1,2,3]
# common = []

# if len(x) > len(y):
#     list_a , list_b = x  ,y
# else:
#     list_a , list_b = y  ,x

# for i in list_a:
#     for j in list_b:
#         if i == j :
#             common.append(i)

# print(common)

# ----------  Write a Python program to remove duplicates from a list.

# x =  [1, 2, 3, 2, 1, 3, 2, 4, 5, 4,2,7,8,5,4,1,2,5,8,9]
# x1 = {}
# for i in x:
#     x1[i] = i
# x2 = list(x1.keys())
# print(x2)
# print(type(x2))



