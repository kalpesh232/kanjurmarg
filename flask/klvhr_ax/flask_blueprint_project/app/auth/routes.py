from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models import User
from ..extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods = ["POST"])
def register():
    data = request.get_json()

    user = User(username = data.get('username'))
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

    return jsonify({'message' : 'User registered successfully'})

@auth_bp.route('/login', methods = ["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username = data.get('username')).first()
    
    if user and User.check_password(user, data.get('password')):
        token = create_access_token(identity=user.id)
        return jsonify({'token' : token})
    return jsonify({'message' : 'Invalid credentials'}), 401 

