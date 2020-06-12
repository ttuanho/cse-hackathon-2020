from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET browser_used = %s
WHERE redirect_id = %s
"""



def update_browser_used(browser_used, redirect_id):
	cur.execute(query, [browser_used, redirect_id])
	CONNECTION.commit()
