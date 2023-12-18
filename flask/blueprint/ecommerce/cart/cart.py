# ecommerce/cart/cart.py
from flask import Blueprint

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/view')
def view_cart():
    return "View Cart"
