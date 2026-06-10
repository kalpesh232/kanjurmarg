"""
SELECT user, score
FROM (
    SELECT
        user,
        score,
        ROW_NUMBER() OVER (PARTITION BY user ORDER BY score DESC) AS rank FROM my_table
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


# ########## monkey paching
class Greeting:
    def greet(self):
        print("Original greeting")

def new_fun(self):
    print("Hi all")

Greeting.greet = new_fun  # Monkey patching

g = Greeting()
g.greet()  # Calls new_fun instead of the original greet method

