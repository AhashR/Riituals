from app.handler import bp
from app.db import select_all, select_one

from flask import abort, flash, redirect, render_template, url_for, g, request, session

# Shows the User the main page of the handler.
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("handler/base.html")