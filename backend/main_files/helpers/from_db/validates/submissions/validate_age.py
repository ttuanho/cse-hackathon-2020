from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT submission_id
FROM submissions
WHERE age = %s
"""


def validate_age_from_submissions(age):
	cur.execute(query, [age])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==age
