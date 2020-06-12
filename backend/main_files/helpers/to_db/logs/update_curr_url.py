from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET curr_url = %s
WHERE log_id = %s
"""



def update_curr_url(curr_url, log_id):
	cur.execute(query, [curr_url, log_id])
	CONNECTION.commit()
