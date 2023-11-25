from marshmallow import fields
from ..Orders import Order
from ..Config import ma

class OrderSchema(ma.SQLAlchemyAutoSchema):
    food_id = fields.Integer(required=True)
    table_no = fields.Integer(required=True)
    timestamp = fields.Date()
    restaurant_id = fields.Integer(required=True)

    class Meta:
        model = Order
