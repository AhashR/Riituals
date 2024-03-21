# File provided by HBO-ICT
from app.auth import bp, add_user, add_admin, update_user, login_required, admin_required, fetch_users, check_location, add_location, fetch_userid, fetch_user
from app.db import select_all, select_one, execute_query

from flask import abort, flash, redirect, render_template, url_for, g, request, session

# Registers a new user in the database
@bp.route('/register', methods=['GET', 'POST'])
@admin_required
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        locationId = check_location(location)
        branchnumber = request.form.get('branchnumber')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
  
        add_user(name, locationId, branchnumber, email, phone, password)
        return redirect(url_for('main.index'))

    return render_template("auth/register.html")

# Registers a new admin in the database
@bp.route('/beheerder', methods=['GET', 'POST'])
def registeradmin():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        result = check_location(location)
        if result is None:
            print("Location not found")
            locationId = None  # Assign a default value to locationId if location is not found
        else:
            locationId = result
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        add_admin(name, locationId, email, phone, password)
        return redirect(url_for('main.index'))

    return render_template("auth/registerbeh.html")

# Edits the user's information
@bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    user = fetch_userid(g.user['userId'])
    if request.method == 'POST':
        userId = g.user['userId']
        name = request.form.get('name')
        location = request.form.get('location')
        locationId = check_location(location)
        branchnumber = request.form.get('branchnumber')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        result = update_user(g.user['userId'], name, locationId, branchnumber, email, phone, password)
        print(result)
        update_user(name, locationId, branchnumber, email, phone, password, userId)
        return redirect(url_for('main.index'))

    return render_template("auth/edit.html", user=user)


# Wijzigen winkelinformatie
@bp.route('/edituser/<int:branchnumber>', methods=['GET', 'POST'])
@login_required
def edituser(branchnumber):
    store = fetch_users(branchnumber)
    if 'user_id' not in session:
        return redirect(url_for('login'))

    storeUserId = select_one('SELECT userId FROM User WHERE branchnumber = %s', (branchnumber,))

    if not storeUserId: 
        flash("U heeft geen toegang tot deze klant, omdat u deze niet heeft aangemaakt.", "error")
        return redirect(url_for('handler.delivery'))
    
    if request.method == 'POST':
        if store:
            name = request.form.get('name')
            location = request.form.get('location')
            locationId = check_location(location)
            emailaddress = request.form.get('emailaddress')
            phone = request.form.get('telephonenumber')
            password = request.form.get('password')
            userId = storeUserId['userId']

            update_user(name, locationId, branchnumber, emailaddress, phone, password, userId)
            flash("Customer information updated successfully.", "success")
            return redirect(url_for('handler.delivery'))
        else:
            flash("Unauthorized update of store data.", "error")
            return redirect(url_for('error_page'))
    
    return render_template("auth/adminedit.html", store=store)

# Winkel verwijderen
@bp.route('/deletestore/<int:branchnumber>')
@login_required
def deleteuser(branchnumber):
    store = fetch_user(branchnumber)
    if store is None:
        abort(404)


    deleteQuery = "DELETE FROM User WHERE branchnumber = %s "
    execute_query(deleteQuery, branchnumber)

    return redirect(url_for('handler.delivery'))


# Logs the user or admin in, based on isHandler
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('emailaddress')
        password = request.form.get('password')
        if not email or not password:
            abort(400)
        user = select_one("SELECT * FROM User WHERE emailaddress = %s", email)
        if user:
            session.clear()
            session['user_id'] = user['userId']
            if user['isHandler']:
                return redirect(url_for('handler.index'))
            else:  
                return redirect(url_for('main.index'))
        flash("E-mailadres of wachtwoord onjuist")
    return render_template("auth/login.html")

# Logs the user out
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

# Function is unused. However, it is preserved in case it is needed later.
@bp.route('/users')
def users():
    users = select_all("SELECT * from User", None)
    return render_template("auth/users.html", users=users)