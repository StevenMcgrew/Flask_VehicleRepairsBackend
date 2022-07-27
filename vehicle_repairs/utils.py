import re

from flask import abort


def is_email_valid(email):
    email_regex_pattern = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
    if not re.fullmatch(email_regex_pattern, email):
        return False
    return True

def is_username_valid(username):
    username_regex_pattern = r"^\w+$"
    if len(username) < 3 or len(username) > 20 or not re.fullmatch(username_regex_pattern, username):
        return False
    return True

def is_password_valid(password):
    if len(password) < 8 or len(password) > 128:
        return False
    return True

def get_email_from_db(User, _email):
    try:
        user = User.query.filter_by(email=_email).first()
        if user:
            return user.email
        return ''
    except Exception as err:
        abort(500, f'Error: {str(err)}')

def get_username_from_db(User, _username):
    try:
        user = User.query.filter_by(username=_username).first()
        if user:
            return user.username
        return ''
    except Exception as err:
        abort(500, f'Error: {str(err)}')
