from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT booking_event_id
FROM booking_events
WHERE submission_id = %s
"""


def validate_submission_id_from_booking_events(submission_id):
	cur.execute(query, [submission_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==submission_id
