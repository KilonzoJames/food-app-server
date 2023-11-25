from .Config import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    contact = db.Column(db.String(20))
    image = db.Column(db.String(255))

    def __init__(self, name, description=None, contact=None, image=None):
        self.name = name
        self.description = description
        self.contact = contact
        self.image = image
