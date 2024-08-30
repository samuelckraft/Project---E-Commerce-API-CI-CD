from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema

from services import productService
from marshmallow import ValidationError

from caching import cache

from utils.util import token_required, role_required

def save():
    try:
        product_data = product_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 400
    
    product_save = productService.save(product_data)
    if product_save is not None:
        return product_schema.jsonify(product_save), 201
    else:
        return jsonify({"message": "Fallback method eror activated", "body":product_data}), 400

@token_required
@role_required('admin')
def find_all():
    products = productService.find_all()
    return product_schema.jsonify(products), 200


def delete_product():
    products = productService.delete_product()
    return product_schema.jsonify(products), 200