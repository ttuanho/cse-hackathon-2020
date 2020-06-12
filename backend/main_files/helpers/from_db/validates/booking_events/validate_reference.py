from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT booking_event_id
FROM booking_events
WHERE reference = %s
"""


def validate_reference_from_booking_events(reference):
	cur.execute(query, [reference])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==reference
