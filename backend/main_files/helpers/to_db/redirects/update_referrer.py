from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET referrer = %s
WHERE redirect_id = %s
"""



def update_referrer(referrer, redirect_id):
	cur.execute(query, [referrer, redirect_id])
	CONNECTION.commit()
