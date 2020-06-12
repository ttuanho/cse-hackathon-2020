from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM booking_events
WHERE  booking_event_id = %s
"""


def delete_booking_events(booking_event_id):
    cur.execute(query, [booking_event_id])
    CONNECTION.commit()
    # cur.close()