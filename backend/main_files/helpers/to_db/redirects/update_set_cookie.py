from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET set_cookie = %s
WHERE redirect_id = %s
"""



def update_set_cookie(set_cookie, redirect_id):
	cur.execute(query, [set_cookie, redirect_id])
	CONNECTION.commit()
