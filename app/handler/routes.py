from app.handler import bp, check_date, userBranchnumber
from app.db import select_all, execute_query, select_one
from app.auth import admin_required, login_required
from flask import abort, flash, redirect, render_template, url_for, g, request, session
from datetime import datetime

# Shows the User the main page of the handler.
@bp.route('/', methods=['GET', 'POST'])
@admin_required
def index():
    return render_template("handler/base.html")

# Shows the user the page of all the stores that are registered in the database.
# Doubles up as a search function, where the user can search for a store by name, location, email or phone number.
@bp.route('/delivery', methods=['GET', 'POST'])
@admin_required
def delivery():
    query = request.args.get('q')
    if query:
        stores = select_all("SELECT * FROM User INNER JOIN Location ON User.locationId = Location.locationid WHERE User.isHandler = 0 AND (branchnumber LIKE %s OR Location.userLocation LIKE %s OR emailaddress LIKE %s OR telephonenumber LIKE %s)", 
                            ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%'))
    else:
        stores = select_all("SELECT * FROM User INNER JOIN Location ON User.locationId = Location.locationid WHERE User.isHandler = 0")
    return render_template("handler/delivery.html", stores=stores)

    # Add the following return statement
    return "Valid response"

# Shows the user an agenda of a store they have selected
@bp.route('/agenda/<int:branchnumber>', methods=['GET', 'POST'])
@admin_required
def agenda(branchnumber):
    return render_template("handler/agenda.html", branchnumber=branchnumber)

@bp.route('/controltower')
def controltower():
    return render_template("handler/controltower.html")

@bp.route('/planning/<int:branchnumber>/<selectedDate>', methods=['GET', 'POST'])
@login_required
def beheerdertijden(branchnumber, selectedDate):
    if request.method == 'POST':
        date = selectedDate
        dateId = check_date(date)
        userId = userBranchnumber(branchnumber)
        arrival_time = request.form['arrivalTime']
        arrival_estimate = request.form['arrivalEstimate']
        departure_time = request.form['departureTime']
        
        # Voeg de gegevens toe aan de tabel Deliveries, gebruikmakend van de geselecteerde winkel
        execute_query("INSERT INTO Deliveries (userId, departureTime, arrivalTime, arrivalEstimate, dateId) VALUES (%s, %s, %s, %s, %s)", (userId, departure_time, arrival_time, arrival_estimate, dateId))
        
        flash('Aflevertijden succesvol toegevoegd', 'success')
        # return redirect(url_for('beheerdertijden'))

    # Als het een GET-verzoek is, haal dan de lijst met winkels op en render de pagina
    stores = select_all("SELECT * FROM User WHERE isHandler = 0")
    return render_template("handler/beheerdertijden.html", stores=stores)





