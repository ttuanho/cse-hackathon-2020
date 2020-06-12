from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT submission_id
FROM submissions
WHERE gender = %s
"""


def validate_gender_from_submissions(gender):
	cur.execute(query, [gender])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==gender
