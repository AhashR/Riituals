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

def user_delivery(dateId, branchnumber, userId, departure_time, arrival_time, arrival_estimate):
    query = "SELECT User.userId FROM Deliveries INNER JOIN User ON User.userId = Deliveries.userId WHERE Deliveries.dateId = %s AND User.branchnumber = %s"
    values = (dateId, branchnumber)
    result = select_one(query, values)
    if result:
        # Edit the pending delivery
        resultquery = "UPDATE Deliveries SET Deliveries.userId = %s, Deliveries.departureTime = %s, Deliveries.arrivalTime = %s, Deliveries.arrivalEstimate = %s WHERE Deliveries.dateId = %s"
        values = (userId, departure_time, arrival_time, arrival_estimate, dateId)
        execute_query(resultquery, values)
    else:
        # Add a new delivery
        query = "INSERT INTO Deliveries (deliveries.userId, Deliveries.departureTime, Deliveries.arrivalTime, Deliveries.arrivalEstimate, Deliveries.dateId) VALUES (%s, %s, %s, %s, %s)"
        values = (userId, departure_time, arrival_time, arrival_estimate, dateId)
        execute_query(query, values)



from app.handler import routes