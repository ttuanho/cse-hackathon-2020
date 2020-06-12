from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET os_version = %s
WHERE redirect_id = %s
"""



def update_os_version(os_version, redirect_id):
	cur.execute(query, [os_version, redirect_id])
	CONNECTION.commit()
