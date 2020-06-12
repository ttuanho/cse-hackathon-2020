from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE referrer = %s
"""


def validate_referrer(referrer):
	cur.execute(query, [referrer])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==referrer
