from flask import jsonify, Blueprint
from ..models import User 

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=["GET"])
def get_users():
    users = User.query.all()
    print("users : ", users)
    return jsonify([{"id" : u.id, "username" : u.username} for u in users])