from .extensions import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(100), nullable = False)

class OrderItem(db.Model):
    __tablename__ = 'orderitems'
    id = db.Column(db.Integer, primary_key = True)
    product_name =db.Column(db.String(100), nullable = False)
    quentity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete="CASCADE"), nullable=False)