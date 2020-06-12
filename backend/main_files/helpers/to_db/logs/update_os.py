from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET os = %s
WHERE log_id = %s
"""



def update_os(os, log_id):
	cur.execute(query, [os, log_id])
	CONNECTION.commit()
