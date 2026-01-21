# # ########### Python supports a variety of operators 
# a = 10
# b = 3
# # -----> Arithmetic Operators
# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.333...
# print(a // b)  # 3
# print(a % b)   # 1
# print(a ** b)  # 1000
# # -----> Comparison Operators
# print(a == b)  # False
# print(a != b)  # True
# print(a > b)   # True
# print(a < b)   # False
# print(a >= b)  # True
# print(a <= b)  # False
# # -----> Logical Operators
# a = False
# b = False
# print(a and b)  # False
# print(a or b)   # True
# print(not a)    # False
# # -----> Assignment Operators
# x = 5
# x += 3  # x = x + 3, so x is now 8
# x -= 2  # x = x - 2, so x is now 6
# x *= 4  # x = x * 4, so x is now 24
# # -----> Bitwise Operators
# x = 5  # 0101 in binary
# y = 8  # 1101 in binary
# print('AND : ', x & y)  # 0000 (0)
# print('OR : ', x | y)  # 1110 (14)
# print('XOR : ', x ^ y)  # 1110 (14)
# print('NOT : ', ~y)     # Inverts bits (complement)
# print('Left shift : ', x << 2) # 0010 0000 (40)
# print('Right shift : ', x >> 2) # 0010 (2)
# # -----> Membership Operators
# list1 = [1, 2, 3, 4]
# print(3 in list1)     # True
# print(5 not in list1) # True
# -----> Identity Operators
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a is b)  # True
# print(a is c)  # False
# print(a == c)  # True

# ########### How to convert python object into string
# # data = 123
# # data = [1, 2, 3]
# # ----- Using str() Function
# # string_data = str(data)
# # print(string_data)  # Output: '123'
# # -----> Using repr() Function
# # string_data = repr(data)
# # print(string_data)  # Output: '[1, 2, 3]'
# data = {'name': 'Alice', 'age': 30}
# # -----> Using json.dumps()
# # import json
# # json_string = json.dumps(data)
# # print(json_string)  # Output: '{"name": "Alice", "age": 30}'
# # ----->  Using pickle.dumps()
# import pickle
# byte_stream = pickle.dumps(data)
# print('byte_stream : ', byte_stream)
# original_data = pickle.loads(byte_stream)
# print('original_data : ', original_data)  # Output: {'name': 'Alice', 'age': 30}
# string_data = byte_stream.decode('latin1')  # Convert bytes to string
# print('string_data : ', string_data)

########## -> JWT + Role-Based Authorization
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = "khsalpeshhindearishchandra"

# Example: user logs in and gets a token
# @app.route("/login", methods=["POST"])
# def login():
#     user = {"username": "kalpesh", "role": "admin"}  # Normally comes from DB
#     token = jwt.encode(user, SECRET_KEY, algorithm="HS256")
#     return jsonify({"token": token})

# # Authorization check
# @app.route("/admin", methods=["GET"])
# def admin_only():
#     token = request.headers.get("Authorization", "").replace("Bearer ", "")
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         if payload.get("role") != "admin":
#             return jsonify({"error": "Access denied"}), 403
#         return jsonify({"message": "Welcome, Admin!"})
#     except Exception as e:
#         return jsonify({"error": "Invalid token"}), 401

# if __name__ == "__main__":
#     app.run(debug=True)


# ##### Scheduler in python

# -----> schedule 
# import schedule
# import time
# def job():
#     print("Task running...")
# schedule.every().day.at("11:33").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# -----> APScheduler (Advanced Python Scheduler)
# from apscheduler.schedulers.blocking import BlockingScheduler

# def job():
#     print("Task running...")

# scheduler = BlockingScheduler()
# scheduler.add_job(job, 'interval', seconds=10)
# scheduler.start()

# -----> time and threading Modules
# import time
# import threading

# def job():
#     print("Task running...")

# def scheduler(interval):
#     while True:
#         job()
#         time.sleep(interval)

# threading.Thread(target=scheduler, args=(10,)).start()











