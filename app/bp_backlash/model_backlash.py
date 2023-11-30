from app import db

class Shimming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pinion_value = db.Column(db.Float(50), nullable=False, default=0)
    backlash_value = db.Column(db.Float(255), nullable=False, default=0)
    shim_left = db.Column(db.Integer, nullable=False, default=0)
    shim_right = db.Column(db.Integer, nullable=False, default=0)
