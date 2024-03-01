from app.handler import bp
from app.db import select_all, execute_query, select_one
from app.auth import admin_required, login_required
from flask import abort, flash, redirect, render_template, url_for, g, request, session
from datetime import datetime

# Shows the User the main page of the handler.
@bp.route('/', methods=['GET', 'POST'])
@admin_required
def index():
    return render_template("handler/base.html")

@bp.route('/delivery', methods=['GET', 'POST'])
@admin_required
def delivery():
    stores = select_all("SELECT * FROM User WHERE isHandler = 0")
    return render_template("handler/delivery.html", stores=stores)

@bp.route('/agenda/<int:branchnumber>', methods=['GET', 'POST'])
@admin_required
def agenda(branchnumber):
    return render_template("handler/agenda.html", branchnumber=branchnumber)
