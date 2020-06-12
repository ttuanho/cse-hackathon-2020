from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET access_time = %s
WHERE log_id = %s
"""



def update_access_time(access_time, log_id):
	cur.execute(query, [access_time, log_id])
	CONNECTION.commit()
