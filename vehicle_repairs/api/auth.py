from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, request, session, abort, jsonify
from ..utils import is_email_valid, is_password_valid, is_username_valid, is_email_available, is_username_available
from ..models.user import User
from ..shared_db import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


############################################
#   Signup
############################################

@bp.post('/signup')
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
    if not is_email_available(User, _email):
        abort(400, 'Someone has already signed up with that email address.')
    if not is_username_available(User, _username):
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
#   Login
############################################

@bp.post('/login')
def login():
    if 'email' not in request.json or 'password' not in request.json:
        abort(400, 'Incomplete JSON data. You must supply email and password.')
    
    _email = request.json['email']
    _password = request.json['password']

    if not is_email_valid(_email):
        abort(400, 'Invalid email address detected.')
    if not is_password_valid(_password):
        abort(400, 'Password must be between 8 and 128 characters in length.')

    user = User.query.filter_by(email=_email).first_or_404()

    if user.status == 'on_hold':
        abort(400, f'The account for {user.username} has been placed on hold.')
    if user.status == 'cancelled':
        abort(400, f'The account for {user.username} was cancelled and is no longer in use.')
    if not check_password_hash(user.password, _password):
        abort(404)

    session.clear()
    session['user_id'] = user.id
    session.permanent = True

    return jsonify(user.serialize())

############################################
#   Logout
############################################

@bp.delete('/logout')
def logout():
    session.clear()
    return jsonify(success=True)
