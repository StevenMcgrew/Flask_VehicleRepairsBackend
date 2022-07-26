from ..shared_db import db
from sqlalchemy.sql import func


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(2000), nullable=False)
    like_count = db.Column(db.Integer, nullable=False, default=0)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now(), onupdate=func.now())

    # def __init__(self, comment: str, post_id: int, user_id: int, ):
    #     self.comment = comment
    #     self.post_id = post_id
    #     self.user_id = user_id