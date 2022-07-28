import uuid

from ..shared_db import db
from flask import Blueprint, request, abort, jsonify, session, g
from ..utils import is_email_valid, is_username_valid, is_email_available, is_username_available
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

@bp.get('/emails/<email>/is-available')
def email_availability(email: str):
    if len(email) > 319:
        abort(400, 'Email address must be less than 320 characters in length.')
    return jsonify(is_available=is_email_available(User, email))


############################################
#   Check username availability
############################################

@bp.get('/usernames/<username>/is-available')
def username_availability(username: str):
    if len(username) > 20:
        abort(400, 'Username must be less than 21 characters in length.')
    return jsonify(is_available=is_username_available(User, username))


############################################
#   Delete user
############################################

@bp.delete('')
def delete_user():
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

