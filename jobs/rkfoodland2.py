#---------- Write a Python function that calculates the factorial of a given number.
# def fact(value):
#     if value == 1 :
#         return value
#     else:
#         return value * fact(value - 1)
         
# print('x : ', fact(7))
#------------ Write a Python script to find the sum of the first 50 prime numbers.

# num = 0
# primt_ls = []
# while True:
#     print('Len : ', len(primt_ls))
#     if len(primt_ls) < 51 :
#         if num == 0 or num == 1 :
#             pass
#         else :
#             for i in range(2,num):
#                 if num % i == 0 :
#                     print('not prime : ', num)
#                     break
#             else:
#                 primt_ls.append(num)
#                 print('prime : ', num)
#         num += 1
#     else :
#         print('final list : ', primt_ls)
#         print('sum of list : ', sum(primt_ls))
#         break

# ----------- Create a Python class representing a Book with properties such as title, author, and publication year. Include a method to display the book details.

# class Book:
# 	def __init__(self, title, author, pub_year):
# 		self.title = title
# 		self. author = author
# 		self. pub_year =  pub_year
# 	def book_details(self):
# 		return  f'title : {self.title} – author : { self.author} – publish year : {self.pub_year}'

# book =  Book('myBooktittle',' kalpesh shinde', '22-12-2023')
# print(book.book_details())

# ---------- Write a Python function that checks if a given string is a palindrome

# name = 'kalpesh'
# if name == name[::-1] :
#     print( f'{name } palindrome' )
# else:
#      print( f'{name } Not palindrome' )

# num = 1223
# stor = num
# temp = 0
# while num > 0 :
#     last_digit = num % 10
#     temp = last_digit + temp * 10
#     num //= 10
#     # print(temp)
# if temp == stor:
#     print( f'{stor } palindrome' )
# else:
#      print( f'{stor } Not palindrome' )

# --------- Create a Python script that reads data from a JSON file and displays it in a formatted way.

# import json

# def display_formatted_data(data):
#     for person in data:
#         print(f"Name : {person['name']}")
#         print(f"Age : {person['age']}")
#         print(f"City : {person['city']}")
#         print('='*20)

# file_path = 'rkfoodland.json'

# try:
#     with open(file_path, 'r') as file:
#         print('file type : ', type(file))
#         print('file : ', (file))
#         data = json.load(file)
#         print('data type : ', type(data))
#         print('data : ', (data))
#         display_formatted_data(data)
#         print('file : ',data)
# except FileNotFoundError:
#     print(f"File not found: {file_path}")
# except json.JSONDecodeError:
#     print(f"Error decoding JSON in file: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# --------- Write a SQL query to find the number of orders placed in each month of the year from the orders table.

'''
select extract(month from order_date) as month , count(order_id) as num_orders from myorders group by extract(month from order_date) order by month;
'''

# ---------- Create a SQL query to retrieve the names and quantities of products that have a quantity higher than the average quantity in the inventory table.

'''
select * from inventory where quantity > (select  avg(quantity) from inventory);
'''

# -------- Write a SQL query to find the average rating of all products from the product_reviews table.

'''
select avg(rating) as 'average_rating ' from product_reviews;
'''

# -------- Write a SQL query to find the top 2 customers who have made the highest total purchases from the orders and order_items tables.

'''
select orders1.customer_id, sum( order_items.price * order_items.quantity) as purchase_sum from orders1 join order_items  on orders1.order_id = order_items.order_id 
group by orders1.customer_id  order by purchase_sum desc limit 2;
'''

            


