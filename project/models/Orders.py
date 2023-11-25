# from sqlalchemy.orm import relationship
from .Config import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, nullable=False)
    table_no = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Date)
    restaurant_id = db.Column(db.Integer, nullable=False)
    
    # food_item = relationship('FoodItem', back_populates='orders')
    # restaurant = relationship('Restaurant', back_populates='orders')

  
