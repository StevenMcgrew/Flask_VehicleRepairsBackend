from ..shared_db import db


class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(40), nullable=False)
    model = db.Column(db.String(40), nullable=False)
    engine = db.Column(db.String(5), nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    