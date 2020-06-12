from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET referrer_type = %s
WHERE log_id = %s
"""



def update_referrer_type(referrer_type, log_id):
	cur.execute(query, [referrer_type, log_id])
	CONNECTION.commit()
