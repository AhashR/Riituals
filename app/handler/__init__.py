from flask import Blueprint
from app.db import execute_query, select_all, select_one
from datetime import datetime

bp = Blueprint('handler', __name__)

# Defines the command create_event, which makes it possible to create an event with a description, event data, creation date
# and uses the participantId to show who the organizer is. It also shows if the event is expired. While totalAmount and paidAmount
# are mentioned in this code, it is not used as it is being shown on overViewPayments.html instead of events.html
def create_event(creator_id: int, description: str, date: datetime):
    query = "INSERT INTO Event (description, eventDate, creationDate, participantId, \
        isExpired, totalAmount, paidAmount) VALUES (%s, %s, %s, %s, 0, 0, 0);"
    execute_query(query, (description, date, datetime.now(), creator_id))
    last_insert = select_one("SELECT LAST_INSERT_ID() AS id")
    return last_insert['id'] if last_insert else None

# Defines the command update_event, which makes it possible to update an event description and date.
def update_event(event_id: int, description: str, date: datetime):
    query = "UPDATE Event SET description = %s, eventDate = %s WHERE eventId = %s"
    execute_query(query, (description, date, event_id))

# Defines the command fetch_event, which retrieves information about an event from a database based on a unique event_id attached to it
def fetch_event(event_id):
    return select_one("SELECT * FROM Event WHERE eventId = %s", event_id)

# Defines the command fetch_participants, which fetches information from participants from the event_id it fetches from.
def fetch_participants(event_id):
    query = "SELECT u.participantId, u.firstname, u.lastname \
        FROM Participant AS u INNER JOIN ParticipantEvent AS p \
        ON u.participantId = p.participantId AND p.eventId = %s"
    return select_all(query, event_id)

# Find all users who are not participants of this event. They
# are candidates for the purpose of adding new participants.
def fetch_candidates(event_id):
    query = "SELECT u.participantId, u.firstname, u.lastname \
        FROM Participant AS u LEFT OUTER JOIN ParticipantEvent AS p \
        ON u.participantId = p.participantId AND p.eventId = %s \
        WHERE p.eventId IS NULL"
    return select_all(query, event_id)

# Defines the command add_participant, which inserts eventId, participantId and userTotal into the table ParticipantEvent.
# userTotal does not have the value %s, but 0, since it allows the database to create a new userTotal of 0 instead of NULL,
# which means that it now registers userTotal as an int instead of a string
def add_participant(event_id, user_id):
    query = "INSERT INTO ParticipantEvent (eventId, participantId, userTotal) VALUES (%s, %s, 0)"
    execute_query(query, (event_id, user_id))

# Defines the command remove_participant, which deletes eventId and participantId from ParticipantEvent.
# Currently, this feature is incomplete and does not work, since it is not yet possible for a user to remove a participant
# Besides that, this script does not clean up transactions or the ParticipantEventId
def remove_participant(event_id, user_id):
    # TO-DO: handle clean up of related transactions
    query = "DELETE FROM ParticipantEvent WHERE eventId = %s AND participantId = %s"
    execute_query(query, (event_id, user_id))
from app.handler import routes