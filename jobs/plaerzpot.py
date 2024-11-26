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
class Parent:
    def __init__(self, value1):
        self.v1 = value1

    def show(self):
        print(f'Parent value1: {self.v1}')

class Child(Parent):
    def __init__(self, value2, value3):
        super().__init__(1)  # Initialize parent class
        self.v2 = value2
        self.v3 = value3  # Child-specific attribute

    def show(self):
        # Including parent attributes in output
        super().show()
        print(f'Child value2: {self.v2}, Child value3: {self.v3}')

c = Child(2, 3)
c.show()


# ########## monkey paching
class greeting:
    def __init__(self):
        print("hello all")

    def greet(self):
        print("Original greeting")

# Monkey patch the greet method to change its behavior
def new_fun(self):
    print("hi all")

# Apply the patch to the class
greeting.greet = new_fun

# Now create an instance of greeting and call the greet method
g = greeting()
g.greet()  # This will now call new_fun instead of the original greet method
