# queue libraries.
# import time
# import threading
# from queue import Queue

# order_queue = Queue()

# def place_order(order_id):
#     print(f"🛒 Order received: {order_id}")
#     order_queue.put(order_id)

# def process_order():
#     while True:
#         order_id = order_queue.get()   # waits if queue is empty
#         print(f"⚙️ Processing order: {order_id}")
#         time.sleep(2)                  # simulate processing time
#         print(f"✅ Order completed: {order_id}")
#         order_queue.task_done()

# worker = threading.Thread(target=process_order, daemon=True)
# worker.start()

# place_order(1201)
# place_order(1202)
# place_order(1203)
# place_order(1204)
# place_order(1205)
# place_order(1206)

# order_queue.join()

# Build Flask REST API
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# items = []
# item_id = 1

# # CREATE
# @app.route("/items", methods=["POST"])
# def create_item():
#     global item_id
#     data = request.get_json()
#     item = {
#         "id": item_id,
#         "name": data["name"]
#     }
#     items.append(item)
#     item_id += 1
#     return jsonify(item), 201

# # READ ALL
# @app.route("/items", methods=["GET"])
# def get_items():
#     return jsonify(items)

# # READ ONE
# @app.route("/items/<int:id>", methods=["GET"])
# def get_item(id):
#     for item in items:
#         if item["id"] == id:
#             return jsonify(item)
#     return jsonify({"error": "Not found"}), 404

# # UPDATE
# @app.route("/items/<int:id>", methods=["PUT"])
# def update_item(id):
#     data = request.get_json()
#     for item in items:
#         if item["id"] == id:
#             item["name"] = data["name"]
#             return jsonify(item)
#     return jsonify({"error": "Not found"}), 404

# # DELETE
# @app.route("/items/<int:id>", methods=["DELETE"])
# def delete_item(id):
#     global items
#     items = [i for i in items if i["id"] != id]
#     return jsonify({"message": "Deleted"})

# if __name__ == "__main__":
#     app.run(debug=True)

# SQLAlchemy models & queries

# # 1️⃣ Model (table)
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)

# # 2️⃣ Create record (INSERT)
# user = User(username="kalpesh")
# db.session.add(user)
# db.session.commit()

# # 3️⃣ Read records (SELECT)
# User.query.all()
# User.query.first()
# User.query.filter_by(username="kalpesh").first()

# # 4️⃣ Update record
# user = User.query.get(1)
# user.username = "newname"
# db.session.commit()

# # 5️⃣ Delete record
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

# JWT auth
# from flask import Flask, jsonify, request
# from flask_jwt_extended import (
#     JWTManager, create_access_token,
#     jwt_required, get_jwt_identity
# )

# app = Flask(__name__)
# app.config["JWT_SECRET_KEY"] = "secret"
# jwt = JWTManager(app)

# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     token = create_access_token(identity=data["username"])
#     return jsonify(access_token=token)

# @app.route("/profile")
# @jwt_required()
# def profile():
#     user = get_jwt_identity()
#     return jsonify(user=user)

# app.run(debug=True)

# Prepare Gunicorn config
bind = "0.0.0.0:8000"

workers = 3              # (2 x CPU cores) + 1
worker_class = "sync"

timeout = 120

accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"

daemon = False



