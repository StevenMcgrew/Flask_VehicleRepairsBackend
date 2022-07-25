import imp
import os

from flask import Flask
from flask_migrate import Migrate
from instance import config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # default config
    app.config.from_mapping(
        SECRET_KEY='change_this_when_deploying',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/vehicle_repairs',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    # override config if needed
    if test_config is None:
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .shared_db import db
    db.init_app(app)
    migrate = Migrate(app, db, directory='vehicle_repairs/migrations')

    # The models need to be imported here for Flask-Migrate to work
    from .models import user

    # Register Blueprints
    # from api import (users as _users,
    #                 comments as _comments)
    # app.register_blueprint(_users.bp)
    # app.register_blueprint(_comments.bp)

    return app