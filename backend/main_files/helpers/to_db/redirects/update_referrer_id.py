from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET referrer_id = %s
WHERE redirect_id = %s
"""



def update_referrer_id(referrer_id, redirect_id):
	cur.execute(query, [referrer_id, redirect_id])
	CONNECTION.commit()
