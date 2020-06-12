from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE submissions
SET description = %s
WHERE submission_id = %s
"""



def update_description(description, submission_id):
	cur.execute(query, [description, submission_id])
	CONNECTION.commit()
