from flask_restful import Resource, Api
from flask import Blueprint, jsonify
from marshmallow import ValidationError
from ..models.Restaurant import Restaurant
from ..models.marshmallow.Res import RestaurantSchema

restaurant_blue = Blueprint('restaurant_api', __name__)
restaurant_api = Api(restaurant_blue)

class RestaurantResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_schema = RestaurantSchema(many=True)
        json_string = restaurant_schema.dump(restaurants)
        return json_string

class RestaurantId(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get_or_404(id)
        schema = RestaurantSchema()
        return schema.dump(restaurant)

restaurant_api.add_resource(RestaurantResource, '/restaurants')
restaurant_api.add_resource(RestaurantId, '/restaurants/<int:id>')

@restaurant_blue.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
