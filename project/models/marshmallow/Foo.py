from marshmallow import fields
from ..Food import FoodItem
from ..Config import ma

class FoodItemSchema(ma.SQLAlchemyAutoSchema):
    food = fields.String(required=True)
    description = fields.String()
    price = fields.Float(required=True)
    origin = fields.String()
    image = fields.String()
    restaurant_id = fields.Integer()

    class Meta:
        model = FoodItem
        load_instance=True
