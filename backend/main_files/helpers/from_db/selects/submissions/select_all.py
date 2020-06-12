from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT * FROM submissions
"""


def select_all_from_submissions():
	cur.execute(query)
	res = None
	res = cur.fetchall()
	return res
