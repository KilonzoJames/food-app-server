# import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from .models.Config import db, migrate, ma

# Register the blueprints for different routes in your app
from .routes.food import food_item_blue
from .routes.restaurant import restaurant_blue
from .routes.orders import order_blue

# Initialize the Flask app
app = Flask(__name__)

# Configure application settings
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///foodapp.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "DELETE", "PATCH"]}}, supports_credentials=True)

# app.config.from_pyfile('config.cfg')
# mail.init_app(app)
# Initialize Flask extensions
api = Api(app)  # Initialize the RESTful API
cors = CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)
db.init_app(app)  # Initialize the SQLAlchemy database
migrate.init_app(app, db)

# Initialize Marshmallow with the Flask app
ma.init_app(app)

# Register the blueprints for different routes in the app
blueprints = [ food_item_blue, order_blue, restaurant_blue ]

for blueprint in blueprints:
    app.register_blueprint(blueprint)

# Run the application on port 5555 in debug mode
if __name__ == '__main__':
    app.run(port=5555, debug=True)