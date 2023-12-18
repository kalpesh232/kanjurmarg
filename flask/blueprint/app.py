# app.py
from flask import Flask
from ecommerce.api.api import api_bp
from ecommerce.auth.auth import auth_bp
from ecommerce.cart.cart import cart_bp
from ecommerce.general.general import general_bp
from ecommerce.products.products import products_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(general_bp)
app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(debug=True)