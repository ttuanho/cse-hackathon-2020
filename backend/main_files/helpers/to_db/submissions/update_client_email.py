from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE submissions
SET client_email = %s
WHERE submission_id = %s
"""



def update_client_email(client_email, submission_id):
	cur.execute(query, [client_email, submission_id])
	CONNECTION.commit()
