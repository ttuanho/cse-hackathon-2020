from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT * FROM doctor_tag_relations
"""


def select_all_from_doctor_tag_relations():
	cur.execute(query)
	res = None
	res = cur.fetchall()
	return res
