from ..shared_db import db
from sqlalchemy.sql import func
from sqlalchemy import FetchedValue, text


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(2000), nullable=False)
    like_count = db.Column(db.Integer, nullable=False, server_default=text('0'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)
    created_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=FetchedValue())

    # def __init__(self, comment: str, post_id: int, user_id: int, ):
    #     self.comment = comment
    #     self.post_id = post_id
    #     self.user_id = user_id