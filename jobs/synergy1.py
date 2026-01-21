

# ----- modify string 
# mystr = "kalpesh"
# ls_str = list(mystr)
# ls_str[3] = 'xxx'
# result = (''.join(ls_str))
# print('ls_str : ', result)


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

# x = [9,7,6,9,9,7,3,7,6,6,9,1,7,2,4,2,6,7,3,1]
# x_dict = {}
# for item in x:
#     if item in x_dict:
#         x_dict[item] += 1
#     else:
#         x_dict[item] = 1

# print('Result:', x_dict)

# --------- Write a Python program to find the common elements between two lists.

# x1 = [9, 7, 6, 9, 9, 7, 3, 7, 6, 6]
# x2 = [9, 1, 7, 2, 4, 2, 6, 7, 3, 1]

# # Using set intersection to find common elements efficiently
# common_elements = set(x1) & set(x2)

# print('Common elements:', common_elements)


# ----------  Write a Python program to remove duplicates from a list.

# x1 = [9,7,6,9,9,7,3,7,6,6,9,1,7,2,4,2,6,7,3,1]
# print('x1 : ', x1)
# set_x = list(dict.fromkeys(x1))
# print('x1 : ', list(set_x))

# ---------- difference between merge, join and concatenate

# import pandas as pd
# import numpy as np

# # dictionary of lists
# dict = {'id':[1, 4, 2, 9,10],
#         'Age': [30, 45, 35, 40,50],
#         'Score':[200, 140, 180, 198,210]}

# # dictionary of lists
# dict1 = {'id':[1, 4, 2, 9,8,6],
#         'Age1': [30, 45, 35, 40,50,45],
#         'Score1':[200, 140, 180, 198,210,209]}

# # creating a DataFrame
# df = pd.DataFrame(dict)
# df1 = pd.DataFrame(dict1)

# # print(df)
# # print(df1)

# # x = pd.merge(df,df1, on='id')
# # x = df1.join(df)
# x = pd.concat([df,df1], axis=1)

# print(x)

# ----------  identify and deal with missing values

# import pandas as pd
# import numpy as np 

# dict = {
#     'id' : [1,4,np.nan, 9],
#     'age' : [30,45,90, 55],
#     'score' : [130,  np.nan, 140, 198]
# }

# df = pd.DataFrame(dict)
# print(df)
# print('')
# # print(df.isnull().sum())
# # drop missing values
# # output = df.dropna(axis = 1, how = 'all')
# # print(output)
# # x = df.dropna()
# # x = df.fillna(00.00)
# # x = df.replace(to_replace=30, value=999)


# print(x)

# ---------- replace string space with a given character in Python

# text = "D t C mpBl ckFrid yS le"
# ch = "a"

# x = text.replace(' ','a')
# print(x)

# ---------- positive integer num, write a function that returns True if num is a perfect square else False

# def valid_sqaure(num):
#     square = int(num**0.5)
#     if square**2 == num :
#         return True
#     return False

# x = int(input('Enter a Number : '))
# result = valid_sqaure(x)
# print(result)

# --------- class representing a Book with properties such as title, author, and publication year. Include a method to display the book details.

# class book():
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def display(self):
#         return f"Book Title : {self.title} | Author : {self.author} | Publish Year : {self.year}"
# b = book('myBook', 'kalpesh','2024')
# result = b.display()
# print(result)




