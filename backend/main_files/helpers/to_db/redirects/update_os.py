from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET os = %s
WHERE redirect_id = %s
"""



def update_os(os, redirect_id):
	cur.execute(query, [os, redirect_id])
	CONNECTION.commit()
