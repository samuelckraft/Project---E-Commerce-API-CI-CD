from flask import Blueprint
from controllers.orderController import save, find_all, delete_order

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=["POST"])(save)

order_blueprint.route('/', methods=["GET"])(find_all)

order_blueprint.route('/', methods=["DELETE"])(delete_order)