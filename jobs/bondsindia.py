# from flask import Flask, render_template, request, jsonify
# from flask_mysqldb import MySQL
# import json

# app = Flask(__name__)

# # MySQL Configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'dummydb'

# mysql = MySQL(app)

# # API endpoint to render HTML form
# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM employees")
#     data = cur.fetchall()
#     print('data : ', data)
#     print('data : ', type(data))
#     data1 = json.dumps(data)
#     print('data1 : ', data1)
#     print('data1 : ', type(data1))
#     cur.close()
#     return 'true'
# # API endpoint to handle form submission
# @app.route('/add_data', methods=['POST'])
# def add_data():
#     try:
#         # Get data from the form
#         name = request.form['name']
#         email = request.form['email']

#         # Insert data into the MySQL table
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO dummytable (name, email) VALUES (%s, %s)", (name, email))
#         mysql.connection.commit()
#         cur.close()

#         return jsonify({"message": "Data added successfully"})

#     except Exception as e:
#         return jsonify({"error": str(e)})

# @app.route('/update/<int:id>')
# def update_email(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM dummytable WHERE id = %s", (id,))
#     data = cur.fetchone()
#     cur.close()
#     return render_template('bondsindia.html', data=data)

# # API endpoint to handle form submission for updating email
# @app.route('/update_email/<int:id>', methods=['PUT'])
# def update_email_submit(id):
#     try:
#         # Get updated data from the request JSON
#         print(id)
#         new_email = request.form['email']
#         print(new_email)
     

#         # Update data in the MySQL table
#         cur = mysql.connection.cursor()

       

#         if new_email:
#             cur.execute("UPDATE dummytable SET email = %s WHERE id = %s", (new_email, id))

#         mysql.connection.commit()
#         cur.close()

#         return jsonify({"message": "Data updated successfully"})

#     except Exception as e:
#         return jsonify({"error": str(e)})


# if __name__ == '__main__':
#     app.run(debug=True)

# ###################### Python json.dumps(): Basic Use ############################################

# import json
# # Define a Python dictionary
# data = {"name": "John", "age": 30}
# print('data : ', data)
# print('dataT : ', type(data))
# # Use json.dumps() to convert the dictionary into a JSON string
# json_data = json.dumps(data)
# print('json_data : ', json_data)
# print('json_dataT : ', type(json_data))
# eggs = json.loads(json_data)
# print('json_data_loads : ', eggs)
# print('json_data_loads T : ', type(eggs))

# if data == json_data :
#     print('basis and dumps same')
# if data == eggs :
#     print('basis and loads same')


# ########## json.dumps(): Handling Complex Python Objects ######################

# Handling_data = {
#   'name': 'John',
#   'age': 30,
#   'pets': ['Dog', 'Cat'],
#   'profile': {
#     'job': 'Engineer',
#     'city': 'New York'
#   }
# }

# print('Handling_data : ', Handling_data)
# print('Handling_data T : ', type(Handling_data))

# # Use json.dumps() to convert the object into a JSON string
# Handling_json_data = json.dumps(Handling_data)

# print('Handling_json_data : ', Handling_json_data)
# print('Handling_json_data T : ', type(Handling_json_data))

# ############### Writing JSON to Files with json.dump() #######################

# # Define a Python dictionary
# dump_data = {'name': 'John', 'age': 30}
# # Use json.dump() to write the dictionary into a JSON file
# with open('bondsindia.json', 'w') as f:
#     json.dump(dump_data, f)
# # Verify the contents of the file
# with open('bondsindia.json', 'r') as f:
#     print('dump : ', f.read())

############### Handling Non-Serializable Types ################

# # Define a Python set
# my_set = {1, 2, 3}
# print('my_set : ', my_set)
# print('my_set T : ', type(my_set))
# # Attempt to use json.dumps() on the set
# try:
#     print('1')
#     json_data = json.dumps(my_set)
#     print('2')
# except TypeError as e:
#     print(f'An error occurred: {e}')

################# Dealing with Special Characters ###############

# # Define a Python string with a backslash
# data = r'C:\Users\John'
# print('backslash : ', data)
# print('backslash T : ', type(data))
# # Use json.dumps() to convert the string into a JSON string
# json_data = json.dumps(data)
# print('json_data_backslash : ', json_data)
# print('json_data_backslash T : ', type(json_data))
# # Print the JSON string
# print(json_data)

######################## .load() #######################

