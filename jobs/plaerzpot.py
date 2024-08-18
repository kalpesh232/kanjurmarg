"""
SELECT user, score
FROM (
    SELECT
        user,
        score,
        ROW_NUMBER() OVER (PARTITION BY user ORDER BY score DESC) AS rank
    FROM my_table
) ranked_scores
WHERE rank <= 2
ORDER BY user, rank;

"""

# ################## __init__
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#         print(f'Object created with value: {self.value}')

# # Creating an object of MyClass
# obj = MyClass(10)

# ########### lambda

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x,y : x+y , numbers)
print(result)

# ########## super method in python

# class Parent:
#     def __init__(self, value):
#         print('value : ', value)
#         self.value = value

#     def show(self):
#         print('3')
#         print('1 : ', self.value)

# class Child(Parent):
#     def __init__(self, valye, extra_value):
#         print('valye : ',valye)
#         print('extra_value : ',extra_value)
#         super().__init__(valye)
#         # self.value = valye
#         self.extra_value = extra_value

#     def show(self):
#         print('4')
#         super().show()
#         print('2 : ', self.extra_value)

# child = Child(10,20)
# child.show()

# ########## monkey paching

# class greeting:
#     def show(self):
#         return "Hello All"
    
# g = greeting()
# print(' 1 : ', g.show())

# def new_show(self):
#     return "hi There"

# greeting.show = new_show

# g = greeting()
# print(' 2 : ', g.show())

# 
