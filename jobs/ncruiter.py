# # CRUD operations.
# from flask import Flask, request, jsonify
# import mysql.connector

# app = Flask(__name__)

# def myConn():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="eavhdi"
#     )

# # CREATE
# @app.route("/user", methods=["POST"])
# def create_user():
#     data = request.json
#     sql = "INSERT INTO ncruiter (username) VALUES (%s)"
#     val = (data["username"],)

#     con = myConn()
#     cur = con.cursor()
#     cur.execute(sql, val)
#     con.commit()

#     return jsonify({"message": "User created"}), 201

# # READ
# @app.route("/user", methods=["GET"])
# def read_users():
#     con = myConn()
#     cur = con.cursor(dictionary=True)
#     cur.execute("SELECT * FROM ncruiter")
#     users = cur.fetchall()
#     return jsonify(users)

# # UPDATE
# @app.route("/user/<int:id>", methods=["PUT"])
# def update_user(id):
#     data = request.json
#     sql = "UPDATE ncruiter SET username=%s WHERE id=%s"
#     val = (data["username"], id)

#     con = myConn()
#     cur = con.cursor()
#     cur.execute(sql, val)
#     con.commit()

#     return jsonify({"message": "User updated"})

# # DELETE
# @app.route("/user/<int:id>", methods=["DELETE"])
# def delete_user(id):
#     con = myConn()
#     cur = con.cursor()
#     cur.execute("DELETE FROM ncruiter WHERE id=%s", (id,))
#     con.commit()

#     return jsonify({"message": "User deleted"})

# if __name__ == "__main__":
#     app.run(debug=True)

# Write unit test for API calls or database operation/queries in python?
# def test_create_user():
#     client = app.test_client()
#     res = client.post("/user", json={"name": "Kalpesh"})
#     assert res.status_code == 201

# mock_conn = MagicMock()
# save_user("Kalpesh", mock_conn)
# mock_conn.cursor().execute.assert_called()

# Atomicity
"""
conn.start_transaction()
try:
    cursor.execute("UPDATE account SET balance = balance - 100 WHERE id = 1")
    cursor.execute("UPDATE account SET balance = balance + 100 WHERE id = 2")
    conn.commit()     # atomic success
except:
    conn.rollback()   # atomic fail

"""

