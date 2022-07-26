from ..shared_db import db


class PostTag(db.Model):
    __tablename__ = 'posts_tags'
    post_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, primary_key=True)
