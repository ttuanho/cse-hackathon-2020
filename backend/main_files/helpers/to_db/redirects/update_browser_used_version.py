from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET browser_used_version = %s
WHERE redirect_id = %s
"""



def update_browser_used_version(browser_used_version, redirect_id):
	cur.execute(query, [browser_used_version, redirect_id])
	CONNECTION.commit()
