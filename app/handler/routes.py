from app.handler import bp, create_event, update_event, add_participant, remove_participant, fetch_event
from app.db import select_all, execute_query, select_one
from app.auth import admin_required, login_required
from app.handler import fetch_participants, fetch_candidates
from flask import abort, flash, redirect, render_template, url_for, g, request, session
from datetime import datetime

# Shows the User the main page of the handler.
@bp.route('/', methods=['GET', 'POST'])
@admin_required
def index():
    return render_template("handler/base.html")

@bp.route('/delivery', methods=['GET', 'POST'])
@admin_required
def delivery():
    stores = select_all("SELECT * FROM User WHERE isHandler = 0")
    return render_template("handler/delivery.html", stores=stores)



# Allows the html file: view.html to load data from Events to show the different events a user is part of
@bp.route('/view/<int:event_id>')
@login_required
def view_page(event_id):
    event = fetch_event(event_id) or abort(404)
    participants = fetch_participants(event_id)
    candidates = fetch_candidates(event_id)
    return render_template('events/view.html', event=event, participants=participants, candidates=candidates)

# This function redirects to user to create.html if they wish to create another event
@bp.route('/create')
@login_required
def create_page():
    return render_template('events/create.html')

# Creates an event with the description, date and event id. It also allows the user to add an participant
@bp.route('/create', methods=['POST'])
@login_required
def create_request():
    description = request.form['description']
    date = datetime.fromisoformat(request.form['date'])
    event_id = create_event(session['user_id'], description, date)
    if not event_id:
        return redirect(url_for('events.index'))
    add_participant(event_id, session['user_id'])
    return redirect(url_for('events.view_page', event_id=event_id))

# This function redirects to user to edit.html if they wish to update an event
@bp.route('/edit/<int:event_id>')
@login_required
def edit_page(event_id):
    event = fetch_event(event_id) or abort(404)
    return render_template('events/edit.html', event=event)

# Allows the user to update an event. This fetches the event id, participantid, user id, description and date and
# allows the user to change this data.
@bp.route('/edit/<int:event_id>', methods=['POST'])
@login_required
def edit_request(event_id):
    event = fetch_event(event_id) or abort(404)
    if event['participantId'] != session['user_id']:
        abort(403)
    description = request.form['description']
    date = datetime.fromisoformat(request.form['date'])
    update_event(event_id, description, date)
    return redirect(url_for('events.view_page', event_id=event_id))

# Defines the command add_participant_request, which adds a participant to an event using an event_id and a user_id,
@bp.route('/add-participant', methods=['POST'])
@login_required
def add_participant_request():
    event_id = request.form['event_id']
    user_id = request.form['user_id']
    event = fetch_event(event_id) or abort(422)
    if event['participantId'] != session['user_id']:
        abort(403)
    add_participant(event_id, user_id)
    return redirect(url_for('events.view_page', event_id=event_id))

# Defines the command remove_participant_request, which removes a participant from an event.
# This only works if the user is logged in, seen by @login_required.
@bp.route('/remove-participant')
@login_required
def remove_participant_request():
    event_id = request.args['event_id']
    user_id = request.args['user_id']
    event = fetch_event(event_id) or abort(422)
    if event['participantId'] != session['user_id']:
        abort(403)
    remove_participant(event_id, user_id)
    return redirect(url_for('events.view_page', event_id=event_id))

# Defines the command removeEvent, which makes it possible for a user to delete an event.
# This only works if the user is logged in, seen by @login_required.
@bp.route('/removeEvent/<int:eventId>')
@login_required
def removeEvent(eventId):
    events = select_all("SELECT * FROM Event WHERE participantId = %s", session['user_id'])
    removeQuery = "DELETE FROM Event WHERE eventId = %s"
    execute_query(removeQuery, eventId)

    query = "UPDATE Event SET deleted = NULL WHERE eventId = %s "
    execute_query(query, eventId)

    return redirect(url_for("events.index", events=events))