from marshmallow import fields
from schema import ma

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    price = fields.Integer(required=True)

    class Meta:
        fields = ("id", "name", "email", "phone")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)