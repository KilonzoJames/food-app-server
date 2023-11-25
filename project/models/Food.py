from sqlalchemy.orm import relationship
from .Config import db

class FoodItem(db.Model):
    __tablename__ = 'food_items'

    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    origin = db.Column(db.String(255))
    image = db.Column(db.String(255))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    # restaurant = relationship('Restaurant', back_populates='food_items')

