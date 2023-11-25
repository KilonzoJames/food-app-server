from flask_restful import Resource, Api
from flask import Blueprint, jsonify
from marshmallow import ValidationError
from ..models.Orders import Order
from ..models.marshmallow.Ord import OrderSchema

order_blue = Blueprint('order_api', __name__)
order_api = Api(order_blue)

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        order_schema = OrderSchema(many=True)
        json_string = order_schema.dump(orders)
        return {"results": json_string}

class OrderId(Resource):
    def get(self, id):
        order = Order.query.get_or_404(id)
        schema = OrderSchema()
        return schema.dump(order)

order_api.add_resource(OrderResource, '/orders')
order_api.add_resource(OrderId, '/orders/<int:id>')

@order_blue.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
