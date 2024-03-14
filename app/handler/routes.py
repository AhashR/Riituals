from app.handler import bp
from app.db import select_all, select_one

from flask import abort, flash, redirect, render_template, url_for, g, request, session

# Shows the User the main page of the handler.
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("handler/base.html")


# Dummy tijdstippen
leveringstijden = ["10:00", "12:00", "14:00"]

@bp.route('/update', methods=['POST'])
def update():
    global leveringstijden
    nieuwe_tijden = request.form.getlist('tijd')

    # Update de tijdstippen
    leveringstijden = nieuwe_tijden

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)