from sqlalchemy.sql import func
from ..shared_db import db
from sqlalchemy.dialects import postgresql


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    repair_steps = db.Column(postgresql.JSONB)
    thumbnail = db.Column(db.String(255))
    is_finished = db.Column(db.Boolean, nullable=False, default=False)
    like_count = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id', ondelete='RESTRICT'), nullable=False)
    created_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now(), onupdate=func.now())

