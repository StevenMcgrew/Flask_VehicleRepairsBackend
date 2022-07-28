import enum

from sqlalchemy.sql import func
from sqlalchemy import FetchedValue, text
from ..shared_db import db


class AcctType(enum.Enum):
    OWNER = 'owner'
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'


class AcctStatus(enum.Enum):
    ACTIVE = 'active'
    ON_HOLD = 'on_hold'
    CANCELLED = 'cancelled'


class UITheme(enum.Enum):
    LIGHT = 'light'
    DARK = 'dark'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(319), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(20), nullable=False, server_default='user')
    status = db.Column(db.String(20), nullable=False, server_default='active')
    profile_pic = db.Column(db.String(255))
    vehicles_history = db.Column(db.ARRAY(db.Integer))
    views_history = db.Column(db.ARRAY(db.Integer))
    following = db.Column(db.ARRAY(db.Integer))
    prefers_notifications = db.Column(db.Boolean, nullable=False, server_default=text('false'))
    theme = db.Column(db.String(20), nullable=False, server_default='light')
    created_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_on = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=FetchedValue())

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'type': self.type,
            'status': self.status,
            'profile_pic': self.profile_pic,
            'vehicles_history': self.vehicles_history,
            'views_history': self.views_history,
            'following': self.following,
            'prefers_notifications': self.prefers_notifications,
            'theme': self.theme
        }