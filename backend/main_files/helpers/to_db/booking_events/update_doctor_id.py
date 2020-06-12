from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE booking_events
SET doctor_id = %s
WHERE booking_event_id = %s
"""



def update_doctor_id(doctor_id, booking_event_id):
	cur.execute(query, [doctor_id, booking_event_id])
	CONNECTION.commit()
