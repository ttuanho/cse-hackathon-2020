from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE submissions
SET gender = %s
WHERE submission_id = %s
"""



def update_gender(gender, submission_id):
	cur.execute(query, [gender, submission_id])
	CONNECTION.commit()
