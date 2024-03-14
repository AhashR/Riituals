from app.main import bp
from flask import request, render_template, url_for, flash, redirect, g
from app.auth import login_required
from app.db import select_all, select_one, execute_query
#Add what needs to be imported here.
 
@bp.route('/')
def index():
    return render_template("index.html")
 
@bp.route('/main/controltower')
def controltower():
    return render_template("controltower.html")


@bp.route('/main/beheerdertijden', methods=['GET', 'POST'])
@login_required
def beheerdertijden():
    if request.method == 'POST':
        # Verwerk het formulier en voeg de gegevens toe aan de database
        store_id = request.form['store']
        arrival_time = request.form['arrivalTime']
        arrival_estimate = request.form['arrivalEstimate']
        departure_time = request.form['departureTime']
        
        # Voeg de gegevens toe aan de tabel Deliveries, gebruikmakend van de geselecteerde winkel
        execute_query("INSERT INTO Deliveries WHERE userId = %s (departureTime, arrivalTime, arrivalEstimate) VALUES (%s, %s, %s)", (departure_time, arrival_time, arrival_estimate, store_id))
        
        flash('Aflevertijden succesvol toegevoegd', 'success')
        # return redirect(url_for('beheerdertijden'))

    # Als het een GET-verzoek is, haal dan de lijst met winkels op en render de pagina
    stores = select_all("SELECT * FROM User WHERE isHandler = 0")
    return render_template("beheerdertijden.html", stores=stores)
 
 
@bp.route('/main/agenda')
def agenda():
    return render_template("agenda.html")



