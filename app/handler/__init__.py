from flask import Blueprint
from app.db import execute_query, select_all, select_one
from datetime import datetime

bp = Blueprint('handler', __name__)


from app.handler import routes