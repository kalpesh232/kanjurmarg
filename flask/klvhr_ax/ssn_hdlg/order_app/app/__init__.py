from flask import Flask
from config import Config
from .extensions import db
from .orders.routes import orders_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(orders_bp, url_prefix = '/order')

    with app.app_context():
        db.create_all()

    return app
    
