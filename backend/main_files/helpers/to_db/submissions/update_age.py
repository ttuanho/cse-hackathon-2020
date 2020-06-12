from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE submissions
SET age = %s
WHERE submission_id = %s
"""



def update_age(age, submission_id):
	cur.execute(query, [age, submission_id])
	CONNECTION.commit()
