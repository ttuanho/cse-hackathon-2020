from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET languages_used = %s
WHERE log_id = %s
"""



def update_languages_used(languages_used, log_id):
	cur.execute(query, [languages_used, log_id])
	CONNECTION.commit()
