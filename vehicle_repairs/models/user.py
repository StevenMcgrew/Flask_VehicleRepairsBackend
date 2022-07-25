import enum

from sqlalchemy.sql import func
from ..shared_db import db


class AcctType(enum.Enum):
    OWNER = 'owner'
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'


class AcctStatus(enum.Enum):
    ACTIVE = 'active'
    ON_HOLD = 'on_hold'
    DELETED = 'deleted'


class UITheme(enum.Enum):
    LIGHT = 'light'
    DARK = 'dark'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    email = db.Column(db.String(319),
                      unique=True,
                      nullable=False)

    username = db.Column(db.String(20),
                         unique=True,
                         nullable=False)

    password = db.Column(db.String(128),
                         nullable=False)

    type = db.Column(db.String(20),
                     nullable=False,
                     default=AcctType.USER)

    status = db.Column(db.String(20),
                       nullable=False,
                       default=AcctStatus.ACTIVE)

    profile_pic = db.Column(db.String(255))

    vehicles_history = db.Column(db.ARRAY(db.Integer))

    views_history = db.Column(db.ARRAY(db.Integer))

    following = db.Column(db.ARRAY(db.Integer))

    prefers_notifications = db.Column(db.Boolean,
                                      nullable=False,
                                      default=False)

    theme = db.Column(db.String(20),
                      nullable=False,
                      default=UITheme.LIGHT)

    created_on = db.Column(db.TIMESTAMP(timezone=True),
                           nullable=False,
                           default=func.now())

    updated_on = db.Column(db.TIMESTAMP(timezone=True),
                           nullable=False,
                           default=func.now(),
                           onupdate=func.now())
