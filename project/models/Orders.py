# from sqlalchemy.orm import relationship
from .Config import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    table_no = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Date)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    
    # food_item = relationship('FoodItem', back_populates='orders')
    # restaurant = relationship('Restaurant', back_populates='orders')

    def __init__(self, food_id, table_no, timestamp, restaurant_id):
        self.food_id = food_id
        self.table_no = table_no
        self.timestamp = timestamp
        self.restaurant_id = restaurant_id
