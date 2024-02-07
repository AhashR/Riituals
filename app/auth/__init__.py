# Code provided by HBO-ICT

from flask import Blueprint, redirect, url_for, session, g
# g see https://flask.palletsprojects.com/en/2.3.x/appcontext/
from app.db import execute_query, select_one
import functools

# Define the blueprint here and name it.
# This name is used in the application
bp = Blueprint('auth', __name__)

def add_user(firstname, lastname, email, phone):
    query = "INSERT INTO User (firstname, lastname, emailaddress, \
        telephonenumber) VALUES (%s, %s, %s, %s)"
    values = (firstname, lastname, email, phone)
    execute_query(query, values)

def update_user(id, firstname, lastname, email, phone):
    query = "UPDATE User SET firstname = %s, lastname = %s, emailaddress = %s, \
        telephonenumber = %s WHERE UserId = %s"
    values = (firstname, lastname, email, phone, id)
    execute_query(query, values)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is not None:
        g.user = select_one("SELECT * FROM User WHERE UserId = %s", user_id)
    else:
        g.user = None

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

from app.auth import routes