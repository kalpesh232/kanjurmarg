# ########## Difference Between Low-Level Design (LLD) and High-Level Design (HLD)
# ------- # High-Level Design Example (HLD)
# class PaymentGateway:
#     def process_payment(self, amount):
#         return f"Processing payment of ₹{amount}"

# class OrderService:
#     def __init__(self):
#         self.payment = PaymentGateway()

#     def place_order(self, amount):
#         return self.payment.process_payment(amount)

# # Simulating order placement
# order = OrderService()
# print(order.place_order(500))

# -------- Low-Level Design (LLD)
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age}"

# # Usage
# user1 = User("Kalpesh", 25)
# print(user1.get_details())  # Output: Name: Kalpesh, Age: 25

# ######## fetch 100 records starting from ID 100

# SELECT * FROM table LIMIT 100, 100;
# records = emp.objects.all()[100:100]
# from django.db.models import Q
# records = emp.objects.filter(Q(id__gt=99) & Q(id__lt=201))

# #########  example of *args and **kwargs
# def example_function(*args, **kwargs):
#     print("Positional arguments (*args):", args)
#     print("Keyword arguments (**kwargs):", kwargs)

#     if len(args) > 3:  # Ensure there are at least 4 positional arguments
#         print("Fourth positional argument:", args[3])  # Index 3 gives the 4th element

# example_function(9,7,6,9,9, name="Kalpesh", sirname="Shinde", age=25)

# #########  Python function to check if a given string has balanced brackets while ignoring non-bracket :
# def is_balanced(s):
#     stack = []
#     bracket_pairs = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in bracket_pairs.values():  # If it's an opening bracket
#             stack.append(char)
#         elif char in bracket_pairs.keys():  # If it's a closing bracket
#             if not stack or stack[-1] != bracket_pairs[char]:
#                 return False
#             stack.pop()
    
#     return not stack  # If stack is empty, all brackets are balanced

# # Test cases
# s1 = "{[()()]}"
# s2 = "AA{()()]{}BB"
# s3 = "{[(AU)()]TS}"
# s4 = "{[()(AHYSIS]}"

# print(f"'{s1}' is balanced: {is_balanced(s1)}")
# print(f"'{s2}' is balanced: {is_balanced(s2)}")
# print(f"'{s3}' is balanced: {is_balanced(s3)}")
# print(f"'{s4}' is balanced: {is_balanced(s4)}")

# ####### Quick Sort in Python:
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr  # Base case: Already sorted

#     pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
#     left = [x for x in arr if x < pivot]  # Elements less than pivot
#     middle = [x for x in arr if x == pivot]  # Elements equal to pivot
#     right = [x for x in arr if x > pivot]  # Elements greater than pivot

#     return quick_sort(left) + middle + quick_sort(right)

# # Example usage
# arr = [3, 6, 8, 10, 1, 2, 1]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]

# ###### API optimization involves improving the performance, scalability, and efficiency of an API.
# ---------- Use Efficient Data Structures
# Inefficient
# data = [1, 2, 3, 4, 5]
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         print(data[i], data[j])

# # Efficient
# from itertools import combinations
# for pair in combinations(data, 2):
#     print(pair)

# ------- Minimize Database Queries

# Inefficient
# for user_id in user_ids:
#     user = User.objects.get(id=user_id)  # Multiple database queries

# # Efficient
# users = User.objects.filter(id__in=user_ids)  # Single database query

# -------- Pagination
# from flask import request, Flask

# app = Flask(__name__)

# @app.route('/items')
# def get_items():
#     page = request.args.get('page', 1, type=int)
#     per_page = request.args.get('per_page', 10, type=int)
#     items = Item.query.paginate(page=page, per_page=per_page) # Represents a table in your database.
#     return {
#         'items': [item.to_dict() for item in items.items],
#         'total_pages': items.pages,
#         'current_page': items.page
#     }

# --------- Reuse database
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/alchemy',echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()