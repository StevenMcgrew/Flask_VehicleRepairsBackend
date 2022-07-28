from operator import imod


import uuid

from ..shared_db import db
from werkzeug.security import generate_password_hash
from flask import Blueprint, request, abort, jsonify, session, g
from ..utils import is_email_valid, is_password_valid, is_username_valid, get_email_from_db, get_username_from_db
from ..models.user import User

bp = Blueprint('users', __name__, url_prefix='/users')


############################################
#   "Pre-load" user before every request
############################################

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
        return
    try:
        g.user = User.query.get(user_id)
    except Exception as err:
        abort(500, f'Error: {str(err)}')


############################################
#   Check email availability
############################################

@bp.get('/emails/<email>')
def get_email(email: str):
    if len(email) > 319:
        abort(400, 'Email address must be less than 320 characters in length.')
    return jsonify(email=get_email_from_db(User, email))


############################################
#   Check username availability
############################################

@bp.get('/usernames/<username>')
def get_username(username: str):
    if len(username) > 20:
        abort(400, 'Username must be less than 21 characters in length.')
    return jsonify(username=get_username_from_db(User, username))


############################################
#   Signup
############################################

@bp.post('')
def signup():
    if 'email' not in request.json or 'username' not in request.json or 'password' not in request.json:
        abort(400, 'Incomplete JSON data. You must supply email, username, and password.')

    _email = request.json['email']
    _username = request.json['username']
    _password = request.json['password']

    if not is_email_valid(_email):
        abort(400, 'Invalid email address detected.')
    if not is_password_valid(_password):
        abort(400, 'Password must be between 8 and 128 characters in length.')
    if not is_username_valid(_username):
        abort(400, 'Username must be between 3 and 20 characters in length, and can only contain letters, numbers, or underscore.')
    if get_email_from_db(User, _email):
        abort(400, 'Someone has already signed up with that email address.')
    if get_username_from_db(User, _username):
        abort(400, 'Someone has already signed up with that username.')

    user = User(
        email=_email,
        username=_username,
        password=generate_password_hash(_password)
    )

    try:
        db.session.add(user)
        db.session.commit()

        # TODO: send verification email

        return jsonify(success=True)

    except Exception as err:
        db.session.rollback()
        abort(500, f'Error: {str(err)}')


############################################
#   Delete user
############################################

@bp.delete('')
def cancel_user():
    if g.user is None:
        abort(400, 'You must be logged in to delete your account.')

    g.user.email = f'deleted_{uuid.uuid4().hex}@email.com'
    g.user.password = 'deleted'
    g.user.status  = 'cancelled'
    g.user.profile_pic = None
    g.user.vehicles_history = None
    g.user.views_history = None
    g.user.following = None

    try:
        db.session.commit()
        session.clear()
        return jsonify(success=True)
    except Exception as err:
        db.session.rollback()
        abort(500, f'Error: {str(err)}')


############################################
#   Update email address
############################################

@bp.put('/email')
def update_email():
    if g.user is None:
        abort(400, 'You must be logged in to update your email address.')
    if 'email' not in request.json:
        abort(400, 'Incomplete JSON data. You must supply email.')

    _email = request.json['email']
    if not is_email_valid(_email):
        abort(400, 'Invalid email address detected.')
    g.user.email = _email

    try:
        db.session.commit()
        return jsonify(success=True)
    except Exception as err:
        db.session.rollback()
        abort(500, f'Error: {str(err)}')


############################################
#   Update username
############################################

@bp.put('/username')
def update_username():
    if g.user is None:
        abort(400, 'You must be logged in to update your username.')
    if 'username' not in request.json:
        abort(400, 'Incomplete JSON data. You must supply username.')

    _username = request.json['username']
    if not is_username_valid(_username):
        abort(400, 'Username must be between 3 and 20 characters in length, and can only contain letters, numbers, or underscore.')
    g.user.username = _username

    try:
        db.session.commit()
        return jsonify(success=True)
    except Exception as err:
        db.session.rollback()
        abort(500, f'Error: {str(err)}')

