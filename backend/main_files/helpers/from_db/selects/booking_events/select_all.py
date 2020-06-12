from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT * FROM booking_events
"""


def select_all_from_booking_events():
	cur.execute(query)
	res = None
	res = cur.fetchall()
	return res
