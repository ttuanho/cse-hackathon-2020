from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT booking_event_id
FROM booking_events
WHERE doctor_id = %s
"""


def validate_doctor_id_from_booking_events(doctor_id):
	cur.execute(query, [doctor_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==doctor_id
