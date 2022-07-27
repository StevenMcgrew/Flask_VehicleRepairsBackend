from werkzeug.security import check_password_hash
from flask import Blueprint, request, session, abort, jsonify
from ..utils import is_email_valid, is_password_valid
from ..models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


############################################
#   Login
############################################

@bp.post('/sessions')
def login():
    _email = request.json['email']
    _password = request.json['password']

    if not is_email_valid(_email):
        abort(400, 'Invalid email address detected.')
    if not is_password_valid(_password):
        abort(400, 'Password must be between 8 and 128 characters in length.')

    user = None
    try:
        user = User.query.filter_by(email=_email).first()
    except Exception as err:
        abort(500, f'Error: {str(err)}')

    if not user:
        abort(400, 'No account with that email address was found.')
    if user.status == 'on_hold':
        abort(400, f'The account for {user.username} has been placed on hold.')
    if user.status == 'cancelled':
        abort(400, f'The account for {user.username} was cancelled and is no longer in use.')
    if not check_password_hash(user.password, _password):
        abort(400, 'Incorrect password.')

    session.clear()
    session['user_id'] = user.id
    session.permanent = True

    return jsonify(vehicles_history=user.vehicles_history,
                   views_history=user.views_history,
                   following=user.following,
                   prefers_notifications=user.prefers_notifications,
                   theme=user.theme)

############################################
#   Logout
############################################

@bp.delete('/sessions')
def logout():
    session.clear()
    return jsonify(success=True)
