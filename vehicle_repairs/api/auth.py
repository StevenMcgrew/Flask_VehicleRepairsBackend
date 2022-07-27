import functools


from ..shared_db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort, jsonify
from ..utils import is_email_valid, is_password_valid, is_username_taken, is_username_valid, is_email_taken
from ..models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

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
        error_message += 'Username must only contain letters, numbers, and optionally an underscore. '

    # Check availability of inputs
    if is_email_taken(User, _email):
        error_message += 'Someone has already signed up with that email address. '
    if is_username_taken(User, _username):
        error_message += 'Someone has already signed up with that username. '

    # Abort if any errors
    if error_message:
        abort(400, error_message)

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
    except BaseException as ex:
        # something went wrong :(
        return jsonify(success=False)



