from flask import Flask
from .extensions import db, jwt
from .auth.routes import auth_bp
from .users.routes import user_bp
from .products.routes import products_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extension
    db.init_app(app)
    jwt.init_app(app)

    # Register Bluprints
    app.register_blueprint(auth_bp,url_prefix = '/auth')
    app.register_blueprint(user_bp,url_prefix = '/users')
    app.register_blueprint(products_bp,url_prefix = '/products')

    with app.app_context():
        db.create_all()

    return app
