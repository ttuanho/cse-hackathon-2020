from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT booking_event_id
FROM booking_events
WHERE booking_event_id = %s
"""


def validate_booking_event_id_from_booking_events(booking_event_id):
	cur.execute(query, [booking_event_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==booking_event_id
