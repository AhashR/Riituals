from app.main import bp
from flask import request, render_template, url_for, redirect, g
from app.auth import login_required
from app.db import select_all, select_one, execute_query
#Add what needs to be imported here.

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/main/controltower')
def controltower():
    return render_template("controltower.html")

@bp.route('/main/agenda')
def agenda():
    return render_template("agenda.html")

@bp.route('/main/dag1')
def dag1():
    return render_template("dag1.html")