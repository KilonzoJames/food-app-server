from flask_restful import Resource, Api
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from ..models.Orders import Order
from ..models.marshmallow.Ord import OrderSchema
from ..models.Config import db

order_blue = Blueprint('order_api', __name__)
order_api = Api(order_blue)

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        order_schema = OrderSchema(many=True)
        json_string = order_schema.dump(orders)
        return json_string
    
    def post(self):
        try:
            # Parse and validate the request data using OrderSchema
            schema = OrderSchema()
            validated_data = schema.load(request.json)

            # Create a new order
            new_order = Order(**validated_data)

            # Add the order to the database
            db.session.add(new_order)
            db.session.commit()

            # Return the newly created order
            result = schema.dump(new_order)
            return result , 201  # HTTP status code for "Created"

        except ValidationError as e:
            return jsonify(e.messages), 400
        
class OrderId(Resource):
    def get(self, id):
        order = Order.query.get_or_404(id)
        schema = OrderSchema()
        return schema.dump(order)
    
    def put(self, id):
        try:
            # Find the order by ID
            order = Order.query.get_or_404(id)

            # Parse and validate the request data using OrderSchema
            schema = OrderSchema()
            validated_data = schema.load(request.json)

            # Update the order attributes
            for field, value in validated_data.items():
                setattr(order, field, value)

            # Commit the changes to the database
            db.session.commit()

            # Return the updated order
            result = schema.dump(order)
            return result

        except ValidationError as e:
            return jsonify(e.messages), 400

    def delete(self, id):
        # Find the order by ID
        order = Order.query.get_or_404(id)

        # Delete the order from the database
        db.session.delete(order)
        db.session.commit()

        return {"msg": "Order deleted"}

# Add the new resource to the API
order_api.add_resource(OrderResource, '/orders')
order_api.add_resource(OrderId, '/orders/<int:id>')

@order_blue.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
