from flask import request, Blueprint, jsonify
from ..extensions import db
from ..models import Order, OrderItem

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=["POST"])
def create_order():
    data = request.get_json()
    try:
        order = Order(customer_name = data["customer_name"])
        db.session.add(order)
        db.session.flush()

        for item in data["items"]:
            orderItem = OrderItem(
                product_name = item["product_name"],
                quentity = item["quentity"],
                order_id = order.id
            )

            db.session.add(orderItem)
        db.session.commit()
        return jsonify({"msg" : "Order crreated"}) , 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e) })
    
@orders_bp.route('/orders', methods = ["GET"])
def get_order():
    orders = OrderItem.query.all()
    return jsonify([{"id" : o.id, "product_name" : o.product_name, "quentity" : o.quentity} for o in orders])