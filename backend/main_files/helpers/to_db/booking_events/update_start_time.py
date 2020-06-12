from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE booking_events
SET start_time = %s
WHERE booking_event_id = %s
"""



def update_start_time(start_time, booking_event_id):
	cur.execute(query, [start_time, booking_event_id])
	CONNECTION.commit()
