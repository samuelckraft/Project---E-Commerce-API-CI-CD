from flask import Blueprint
from controllers.customerController import save, find_all, delete_customer

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=["POST"])(save)

customer_blueprint.route('/', methods=["GET"])(find_all)

customer_blueprint.route('/delete', methods=["DELETE"])(delete_customer)
