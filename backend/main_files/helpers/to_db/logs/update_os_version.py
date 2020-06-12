from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET os_version = %s
WHERE log_id = %s
"""



def update_os_version(os_version, log_id):
	cur.execute(query, [os_version, log_id])
	CONNECTION.commit()
