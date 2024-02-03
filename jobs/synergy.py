# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/example', methods=['GET', 'HEAD'])
# def example():
#     response_body = "This is the response body for the GET request."
#     print('request.method : ', request.method)
#     if request.method == 'HEAD':
#         # For a HEAD request, return only the headers without the body
#         return '', 200, {'Content-Length': len(response_body)}

#     # For a regular GET request, return both headers and the response body
#     return response_body

# if __name__ == '__main__':
#     app.run(debug=True)

# ----------------------------------------------- X ---------------------------------------------------

# ---------- Cron job
# from apscheduler.schedulers.background import BackgroundScheduler

# # Create a scheduler
# scheduler = BackgroundScheduler(daemon=True)

# # Define the task
# def my_cron_job():
#     print("Cron job executed!")

# # Schedule the task to run every minute
# scheduler.add_job(my_cron_job, 'cron', minute='*')

# # Start the scheduler
# scheduler.start()

# # Keep the script running
# try:
#     while True:
#         pass
# except (KeyboardInterrupt, SystemExit):
#     # Shut down the scheduler gracefully on interruption
#     scheduler.shutdown()

# ----------- dict to list
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# myList = list(thisdict.items())
# print(myList[1])

# ---------- veriable lenght argument 

# # def myFun(*argv):
# def myFun(**argv):
# 	print(argv)
# 	# for arg in argv:
# 	for arg , arg1 in argv.items():
# 		print(arg, ' ', arg1)


# # myFun('Hello', 'Welcome', 'to', 'kalpeshforkalpesh')
# myFun(first = 'Hello', second = 'Welcome',  third =  'to', fourth = 'kalpeshforkalpesh')
# # myFun({'first' : 'Hello', 'second' : 'Welcome',  'third' :  'to', 'fourth' : 'kalpeshforkalpesh'})

# def myFun(arg1, *argv):
	# print("First argument :", arg1)
	# print("rest argument :", *argv)
# 	for arg in argv:
# 		print("Next argument through *argv :", arg)


# myFun('Hello', 'Welcome', 'to', 'kalpeshforkalpesh')

# def myFun(**kwargs):            # sidha sidha 
# # def myFun(*kwargs):
# 	# for key, value in kwargs.items():
#     print(kwargs)
# 		# for i in kwargs:
# 			# print('i :', i)
# 		# print("%s == %s" % (key, value))


# # Driver code
# myFun(first='kalpesh', mid='for', last='kalpesh')
# # myFun(1,2,3,4,5,6,7,8,9)

# def myFun(arg1, **kwargs):
# 	print("1 :", arg1)
# 	print("2 :", kwargs)
# 	print("3 :", *kwargs)
# 	for key, value in kwargs.items():
# 		print("%s == %s" % (key, value))


# # Driver code
# myFun("Hi", first='kalpesh', mid='for', last='kalpesh')

# def myFun(arg1, arg2, arg3):  # dict
# 	print("arg1:", arg1)
# 	print("arg2:", arg2)
# 	print("arg3:", arg3)


# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("kalpesh", "for", "kalpesh")
# print(*args)
# # myFun(*args)
# # myFun("kalpesh", "for", "kalpesh")

# kwargs = {"arg1": "kalpesh", "arg2": "for", "arg3": "kalpesh"}
# # kwargs = (first='kalpesh', mid='for', last='kalpesh')
# myFun(**kwargs)


# def myFun(a,*args, **kwargs):
# 	print('a : ', a)
# 	print("args: ", args)
# 	print("kwargs: ", kwargs)


# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun(1,'kalpesh', 'for', 'kalpesh', first="kalpesh", mid="for", last="kalpesh")

# # defining car class
# class car():
# 	# args receives unlimited no. of arguments as an array
# 	def __init__(self, *args):
# 	# def __init__(self, args,args1):
# 		print(*args)
# 		print('args : ',  args)
# 		# access args index like array does
# 		self.speed = args[0]
# 		print('self.speed  : ', self.speed )
# 		self.color = args[1]
# 		self.price = args[2]
# 		# self.speed = args
# 		# self.color = args1


# # creating objects of car class
# audi = car(200, 'red', 1000)
# bmw = car(250, 'black', 2000)
# mb = car(190, 'white', 3000)

# # printing the color and speed of the cars
# print(audi.speed)
# print(bmw.speed)
# print(mb.price)

# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, **kwargs):
		# access args index like array does
		self.speed = kwargs['s']
		self.color = kwargs['c']


# creating objects of car class
audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)









# -------------- merge (concatenate) two lists 
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1)

# ----------------------- merge (combine) two dictionaries in Python

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# dict1.update(dict2)
# print(dict1)

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# merged_dict = {**dict1, **dict2}
# print(merged_dict)

