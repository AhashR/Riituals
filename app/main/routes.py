from app.main import bp
from flask import request, render_template, url_for, redirect, g
from app.auth import login_required
from app.db import select_all, select_one, execute_query
#Add what needs to be imported here.

@bp.route('/')
def index():
    if g.user is not None and g.user['isHandler']:
        return redirect(url_for('handler.index'))
    return render_template("index.html")


