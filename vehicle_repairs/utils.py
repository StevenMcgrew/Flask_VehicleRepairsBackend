import re

from sqlalchemy import true


def is_email_valid(email):
    email_regex_pattern = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
    if not re.fullmatch(email_regex_pattern, email):
        return False
    return True

def is_username_valid(username):
    username_regex_pattern = r"^\w+$"
    if username < 3 or username > 20 or not re.fullmatch(username_regex_pattern, username):
        return False
    return True

def is_password_valid(password):
    if len(password) < 8 or len(password) > 128:
        return False
    return True

def is_email_taken(User, _email):
    user_with_that_email = User.query.filter_by(email=_email).first()
    if user_with_that_email:
        return True
    return False

def is_username_taken(User, _username):
    user_with_that_username = User.query.filter_by(username=_username).first()
    if user_with_that_username:
        return True
    return False
