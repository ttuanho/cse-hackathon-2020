from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE booking_events
SET end_time = %s
WHERE booking_event_id = %s
"""



def update_end_time(end_time, booking_event_id):
	cur.execute(query, [end_time, booking_event_id])
	CONNECTION.commit()
