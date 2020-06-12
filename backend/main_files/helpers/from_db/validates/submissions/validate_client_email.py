from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT submission_id
FROM submissions
WHERE client_email = %s
"""


def validate_client_email_from_submissions(client_email):
	cur.execute(query, [client_email])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==client_email
