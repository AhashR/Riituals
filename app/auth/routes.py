# File provided by HBO-ICT
from app.auth import bp, add_user, update_user, login_required
from app.db import select_all, select_one

from flask import abort, flash, redirect, render_template, url_for, g, request, session

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # Add the required multiline docstring here
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        add_user(firstname, lastname, email, email != '', phone)
        return redirect(url_for('main.index'))

    return render_template("auth/register.html")

@bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('emailaddress')
        phone = request.form.get('telephonenumber')
        password = request.form.get('password')
        update_user(g.user['UserId'], firstname, lastname, email, email != '', phone)
        return redirect(url_for('auth.edit'))

    return render_template("auth/edit.html", user=g.user)

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
            session['user_id'] = user['UserId']
            return redirect(url_for('events.index'))
        flash("E-mailadres of wachtwoord onjuist")
    return render_template("auth/login.html")

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@bp.route('/users')
def users():
    users = select_all("SELECT * from User", None)
    return render_template("auth/users.html", users=users)
