from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT booking_event_id
FROM booking_events
WHERE start_time = %s
"""


def validate_start_time_from_booking_events(start_time):
	cur.execute(query, [start_time])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==start_time
