from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET langs_used = %s
WHERE log_id = %s
"""



def update_langs_used(langs_used, log_id):
	cur.execute(query, [langs_used, log_id])
	CONNECTION.commit()
