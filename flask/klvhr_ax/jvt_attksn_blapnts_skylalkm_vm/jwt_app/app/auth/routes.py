from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    
    user = User(username = data.get("username"))
    user.set_password(data.get("password"))

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg" : "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username = data.get("username")).first()
    print("user :------------------------------------ ",  user)

    if not user or not user.check_password(data.get("password")):
        return jsonify({"msg" : "Invalid Credentials"}), 401
    
    token = create_access_token(identity=user.id)
    return jsonify(accessToken = token)

#  Protected API
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        "id" : user.id,
        "username" : user.username
    })