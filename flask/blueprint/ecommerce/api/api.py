# ecommerce/api/api.py
from flask import Blueprint

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/endpoint')
def api_endpoint():
    return "API Endpoint"