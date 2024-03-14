# File provided by HBO-ICT
from app.auth import bp, add_user, add_admin, update_user, login_required
from app.db import select_all, select_one

from flask import abort, flash, redirect, render_template, url_for, g, request, session

# Registers a new user in the database
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if not g.isHandler:
        abort(403)
        
    # Add the required multiline docstring here
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        branchnumber = request.form.get('branchnumber')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        add_user(name, location, branchnumber, email, phone, password)
        return redirect(url_for('main.index'))

    return render_template("auth/register.html")

# Registers a new admin in the database
@bp.route('/beheerder', methods=['GET', 'POST'])
def registeradmin():
    # Add the required multiline docstring here
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        branchnumber = request.form.get('branchnumber')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        add_admin(name, location, branchnumber, email, phone, password)
        return redirect(url_for('main.index'))

    return render_template("auth/registerbeh.html")

# Edits the user's information
@bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        userId = g.user['userId']
        name = request.form.get('name')
        location = request.form.get('location')
        branchnumber = request.form.get('branchnumber')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        result = update_user(g.user['userId'], name, location, branchnumber, email, phone, password)
        print (result)
        update_user(name, location, branchnumber, email, phone, password, userId)
        return redirect(url_for('main.index'))

    return render_template("auth/edit.html", user=g.user)



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