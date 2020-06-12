from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET referrer_type = %s
WHERE redirect_id = %s
"""



def update_referrer_type(referrer_type, redirect_id):
	cur.execute(query, [referrer_type, redirect_id])
	CONNECTION.commit()
