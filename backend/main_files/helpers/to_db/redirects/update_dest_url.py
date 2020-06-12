from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET dest_url = %s
WHERE redirect_id = %s
"""



def update_dest_url(dest_url, redirect_id):
	cur.execute(query, [dest_url, redirect_id])
	CONNECTION.commit()
