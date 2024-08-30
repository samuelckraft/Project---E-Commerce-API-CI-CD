from flask import Flask
from database import db
from schema import ma

from models.customer import Customer
from models.customerAccount import CustomerAccount
from sqlalchemy.orm import Session

from routes.customerBP import customer_blueprint
from routes.customerAccountBP import customer_account_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.customerAccountBP import customer_account_blueprint

from limiter import limiter

from caching import cache

from models.customerManagementRole import CustomerManagementRole
from models.roles import Role

from flask_cors import CORS
from werkzeug.security import generate_password_hash


from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'E-Commerce API'
    }
)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(customer_account_blueprint, url_prefix='/accounts')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)




if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)


    with app.app_context():
        db.create_all()

    app.run(debug=True)