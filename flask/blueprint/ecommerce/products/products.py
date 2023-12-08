# ecommerce/products/products.py
from flask import Blueprint, render_template

products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@products_bp.route('/')
def list_products():
    return render_template('products/list.html')

@products_bp.route('/view/<int:product_id>')
def view_product(product_id):
    return render_template('products/view.html', product_id=product_id)
