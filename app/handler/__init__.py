from flask import Blueprint
from app.db import execute_query, select_all, select_one
from datetime import datetime

bp = Blueprint('handler', __name__)

def check_date(arrivalDate):
    result = select_one("SELECT dateId FROM Deliverydate WHERE arrivalDate = %s", arrivalDate)
    if result is None:
        query = "INSERT INTO Deliverydate (arrivalDate) VALUES (%s)"
        values = (arrivalDate)
        execute_query(query, values)
        result = select_one("SELECT dateId FROM Deliverydate WHERE arrivalDate = %s", arrivalDate)
    return result['dateId']

def userBranchnumber(branchnumber):
    result = select_one("SELECT userId FROM User WHERE branchnumber = %s", branchnumber)
    return result['userId']


from app.handler import routes