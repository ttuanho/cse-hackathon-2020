from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET referrer = %s
WHERE log_id = %s
"""



def update_referrer(referrer, log_id):
	cur.execute(query, [referrer, log_id])
	CONNECTION.commit()
