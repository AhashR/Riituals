from flask import Blueprint

bp = Blueprint('handler', __name__)

from app.handler import routes