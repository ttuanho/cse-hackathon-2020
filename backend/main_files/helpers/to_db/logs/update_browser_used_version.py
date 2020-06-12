from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET browser_used_version = %s
WHERE log_id = %s
"""



def update_browser_used_version(browser_used_version, log_id):
	cur.execute(query, [browser_used_version, log_id])
	CONNECTION.commit()
