from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = "1k3a8l12p19e22s24h27"

users = {
    "admin" : "password"
}

items  = []
item_id_counter = 1

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.headers.get("Authorization")
        print("token -----------------------", token)
        if not token:
            return jsonify({"error" : "Token Missing"}), 401
        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
        except:
            return jsonify({"error" : "Invalid or Expaired token"}), 401 
        
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods = ["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) != password :
        return jsonify({"error" : "Invalid Credentials"}), 401
    token = jwt.encode(
        {
            "user" : username,
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )
    return jsonify({'token' : token})

@app.route('/items', methods=["POST"])
@token_required
def create_item():
    global item_id_counter
    data = request.get_json()
    item = {
        "id" : item_id_counter,
        "name" : data.get("name"),
        "price" : data.get("price")
    }
    items.append(item)
    item_id_counter += 1
    return jsonify(items), 201

@app.route('/items', methods=["GET"])
@token_required
def get_items():
    return jsonify(items)

@app.route('/item/<int:item_id>', methods=["GET"])
@token_required
def get_item(item_id):
    global items
    for item in items:
        print("*"*25, item)
        if item["id"] == item_id :
            return jsonify(item)
    return jsonify({"error" : "Itom not found"}), 404
    
@app.route('/item/<int:item_id>', methods = ["PUT"])
@token_required
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item["id"] == item_id :
            item["name"] = data.get("name", item["name"])
            item["price"] = data.get("price", item["price"])
            return jsonify(item)
    return jsonify({"error" : "Itom not found"}), 404
    
@app.route('/item/<int:item_id>', methods=['DELETE'])
@token_required
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message" : "Item Deleted"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



