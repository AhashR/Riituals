# Code provided by HBO-ICT
from flask import Flask
from app.db import read_db_config, close_db

def create_app():
    app = Flask(__name__)
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    app.config['SECRET_KEY'] = 'MYVERYLONGSECRET'
    app.config['MYSQL_CONFIG'] = read_db_config('instance/db.config')

    app.teardown_appcontext(close_db)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    # Define a blueprint and use a prefix in the URL for it.
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Add your own blueprints here. Remember: at least 1 per team member
    #from app.MYBLUEPRINT import bp as events_bp
    #app.register_blueprint(MYBLUEPRINT.bp, url_prefix='/MYBLUEPRINT')

    return app
