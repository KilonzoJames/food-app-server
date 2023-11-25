from flask_restful import Resource, Api
from flask import Blueprint, jsonify
from marshmallow import ValidationError
from ..models.Food import FoodItem
from ..models.marshmallow.Foo import FoodItemSchema

food_item_blue = Blueprint('food_item_api', __name__)
food_item_api = Api(food_item_blue)

class FoodItemResource(Resource):
    def get(self):
        food_items = FoodItem.query.all()
        food_item_schema = FoodItemSchema(many=True)
        json_string = food_item_schema.dump(food_items)
        return json_string

class FoodItemId(Resource):
    def get(self, id):
        food_item = FoodItem.query.get_or_404(id)
        schema = FoodItemSchema()
        return schema.dump(food_item)

food_item_api.add_resource(FoodItemResource, '/fooditems')
food_item_api.add_resource(FoodItemId, '/fooditems/<int:id>')

@food_item_blue.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
