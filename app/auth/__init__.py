# Code provided by HBO-ICT
from flask import Blueprint, redirect, url_for, session, g
# g see https://flask.palletsprojects.com/en/2.3.x/appcontext/
from app.db import execute_query, select_one, select_all
import functools
from flask import Blueprint
from functools import wraps
from flask import session, redirect, url_for

bp = Blueprint('auth', __name__)

def check_location(location):
    result = select_one("SELECT locationId FROM Location WHERE userLocation = %s", location)
    if result is None:
        query = "INSERT INTO Location (userLocation) VALUES (%s)"
        values = (location)
        execute_query(query, values)
        result = select_one("SELECT locationId FROM Location WHERE userLocation = %s", location)
    return result['locationId']

def add_location(location):
    query = "INSERT INTO Location (location) VALUES (%s)"
    values = (location,)
    execute_query(query, values)

def add_user(name, locationId, branchnumber, email, phone, password):
    query = "INSERT INTO User (name, locationId, branchnumber, emailaddress, telephonenumber, password, isHandler) VALUES (%s, %s, %s, %s, %s, %s, 0)"
    values = (name, locationId, branchnumber, email, phone, password)
    execute_query(query, values)

def add_admin(name, locationId, branchnumber, email, phone, password):
    query = "INSERT INTO User (name, locationId, branchnumber, emailaddress, telephonenumber, password, isHandler) VALUES (%s, %s, %s, %s, %s, %s, 1)"
    values = (name, locationId, branchnumber, email, phone, password)
    execute_query(query, values)
    
# gebruiker gegevens aanpassen zoals naam en wachtwoord gegevens #
def update_user(name, locationId, branchnumber, email, phone, password, userId):
    query = "UPDATE User SET name = %s, locationId = %s, branchnumber = %s, emailaddress = %s, telephonenumber = %s, password = %s WHERE userId = %s"
    values = (name, locationId, branchnumber, email, phone, password, userId)
    execute_query(query, values)

# Selects all users that are not handlers and have the same branchnumber
def fetch_users(branchnumber):
    return select_all("SELECT * FROM User INNER JOIN Location ON User.locationId = Location.locationId WHERE User.isHandler = 0 AND branchnumber = %s", (branchnumber,))

# Selects the user where the userId is equal to the userId
def fetch_userid(userId):
  return select_one("SELECT * FROM User INNER JOIN Location ON User.locationId = Location.locationId WHERE User.userId = %s", (userId,))

# Defines the update_user command, which
# updates user information. The user can change their first name, last name, emailadress, password and telephonenumber.
def admin_update_user(name, location, branchnumber, emailaddress, phone, password, userId):
    query = "UPDATE User SET name = %s, location= %s, branchnumber = %s, emailaddress = %s, telephonenumber = %s, password = %s \
       WHERE userId = %s"
    values = (name, location, branchnumber, emailaddress, phone, password, userId)
    execute_query(query, values)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
        g.isHandler = None
    else:
        g.user = select_one("SELECT * FROM User WHERE userId = %s", user_id)
        if g.user is None:
            g.isHandler = None
        else:
            g.isHandler = g.user['isHandler']

# je moet ingelogd zijn om bepaalde functie te gebruiken #
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('main.index'))
        return view(**kwargs)
    return wrapped_view

def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None or g.isHandler == 0:
            return redirect(url_for('main.index'))
        return view(**kwargs)
    return wrapped_view

from flask import send_file

from app.auth import routes