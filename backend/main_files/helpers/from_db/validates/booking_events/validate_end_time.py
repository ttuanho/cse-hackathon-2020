from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT booking_event_id
FROM booking_events
WHERE end_time = %s
"""


def validate_end_time_from_booking_events(end_time):
	cur.execute(query, [end_time])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==end_time
