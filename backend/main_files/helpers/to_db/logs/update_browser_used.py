from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET browser_used = %s
WHERE log_id = %s
"""



def update_browser_used(browser_used, log_id):
	cur.execute(query, [browser_used, log_id])
	CONNECTION.commit()
