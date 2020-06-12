from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET access_time = %s
WHERE redirect_id = %s
"""



def update_access_time(access_time, redirect_id):
	cur.execute(query, [access_time, redirect_id])
	CONNECTION.commit()
