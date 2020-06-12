from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET dest_url = %s
WHERE log_id = %s
"""



def update_dest_url(dest_url, log_id):
	cur.execute(query, [dest_url, log_id])
	CONNECTION.commit()
