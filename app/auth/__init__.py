# Code provided by HBO-ICT
from flask import Blueprint, redirect, url_for, session, g
# g see https://flask.palletsprojects.com/en/2.3.x/appcontext/
from app.db import execute_query, select_one
import functools
from flask import Blueprint
from functools import wraps
from flask import session, redirect, url_for

bp = Blueprint('auth', __name__)

def add_user(firstname, lastname, email, phone, password):
    query = "INSERT INTO User (firstname, lastname, emailaddress, telephonenumber, password) VALUES (%s, %s, %s, %s, %s)"
    values = (firstname, lastname, email, phone, password)
    execute_query(query, values)

    
# gebruiker gegevens aanpassen zoals naam en wachtwoord gegevens #
def update_user(id, firstname, lastname, email, phone, password):
    query = "UPDATE User SET firstname = %s, lastname = %s, emailaddress = %s, \
        telephonenumber = %s, password = %s WHERE userId = %s"
    values = (firstname, lastname, email, phone, password, id)
    execute_query(query, values)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is not None:
        g.user = select_one("SELECT * FROM User WHERE userId = %s", user_id)
    else:
        g.user = None
# je moet ingelogd zijn om bepaalde functie te gebruiken #
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

from flask import send_file

from app.auth import routes