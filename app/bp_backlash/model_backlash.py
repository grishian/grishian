from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    profile_type = db.Column(db.Integer, default=1)
    date_added = db.Column(db.DateTime, default=datetime.now())