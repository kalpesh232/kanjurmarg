from flask import Blueprint, jsonify
from ..models import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def get_products():
    products = Product.query.all()
    return jsonify([{"id" : p.id, "name" : p.name, "price" : p.price} for p in products])