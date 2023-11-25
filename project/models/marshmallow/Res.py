from marshmallow import fields
from ..Restaurant import Restaurant
from ..Config import ma

class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True)
    description = fields.String()
    contact = fields.String()
    image = fields.String()

    class Meta:
        model = Restaurant
        load_instance=True

