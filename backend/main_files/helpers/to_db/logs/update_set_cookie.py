from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET set_cookie = %s
WHERE log_id = %s
"""



def update_set_cookie(set_cookie, log_id):
	cur.execute(query, [set_cookie, log_id])
	CONNECTION.commit()
