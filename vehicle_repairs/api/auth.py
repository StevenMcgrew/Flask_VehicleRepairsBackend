import functools

from ..shared_db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort, jsonify
from ..utils import is_email_valid, is_password_valid, is_username_available, is_username_valid, is_email_available
from ..models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.get('/email/<email>/is_available')
def check_email_availability(email: str):
    return jsonify(is_available=is_email_available(User, email))

@bp.get('/username/<username>/is_available')
def check_username_availability(username: str):
    return jsonify(is_available=is_username_available(User, username))

@bp.post('/signup')
def signup():
    _email = request.json['email']
    _username = request.json['username']
    _password = request.json['password']
    error_message = ''

    # Validate inputs
    if not is_email_valid(_email):
        error_message += 'Invalid email address detected. '
    if not is_password_valid(_password):
        error_message += 'Password must be between 8 and 128 characters in length. '
    if not is_username_valid(_username):
        error_message += 'Username must be between 3 and 20 characters in length, and can only contain letters, numbers, or underscore. '

    # Check availability of inputs
    if is_email_available(User, _email):
        error_message += 'Someone has already signed up with that email address. '
    if is_username_available(User, _username):
        error_message += 'Someone has already signed up with that username. '

    # Abort if any errors
    if error_message:
        abort(400, f'Errors: {error_message}')

    # Hash the password
    _password = generate_password_hash(_password)

    # Create new user
    user = User(
        email=_email,
        username=_username,
        password=_password
    )

    # Save to db
    try:
        db.session.add(user)
        db.session.commit()
        # TODO: send verification email
        return jsonify(success=True)
    except Exception as err:
        db.session.rollback()
        abort(500, f'Error: {str(err)}')



