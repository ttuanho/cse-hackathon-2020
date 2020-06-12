from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT * FROM tags
"""


def select_all_from_tags():
	cur.execute(query)
	res = None
	res = cur.fetchall()
	return res
