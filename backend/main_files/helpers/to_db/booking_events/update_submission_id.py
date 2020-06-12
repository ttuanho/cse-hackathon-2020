from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE booking_events
SET submission_id = %s
WHERE booking_event_id = %s
"""



def update_submission_id(submission_id, booking_event_id):
	cur.execute(query, [submission_id, booking_event_id])
	CONNECTION.commit()
