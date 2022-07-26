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
    from .models import user, post, comment, vehicle, tag, post_tag

    # Register Blueprints
    from api import (auth, users, posts, comments, vehicles)
    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(comments.bp)
    app.register_blueprint(vehicles.bp)

    return app