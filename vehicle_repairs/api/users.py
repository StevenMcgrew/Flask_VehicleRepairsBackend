from ..shared_db import db
from werkzeug.security import generate_password_hash
from flask import Blueprint, request, abort, jsonify
from ..utils import is_email_valid, is_password_valid, is_username_valid, get_email_from_db, get_username_from_db
from ..models.user import User

bp = Blueprint('users', __name__, url_prefix='/users')


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