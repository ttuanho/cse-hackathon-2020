from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT * FROM doctors
"""


def select_all_from_doctors():
	cur.execute(query)
	res = None
	res = cur.fetchall()
	return res
