from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE booking_events
SET reference = %s
WHERE booking_event_id = %s
"""



def update_reference(reference, booking_event_id):
	cur.execute(query, [reference, booking_event_id])
	CONNECTION.commit()
