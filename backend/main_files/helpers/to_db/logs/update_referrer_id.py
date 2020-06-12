from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET referrer_id = %s
WHERE log_id = %s
"""



def update_referrer_id(referrer_id, log_id):
	cur.execute(query, [referrer_id, log_id])
	CONNECTION.commit()
