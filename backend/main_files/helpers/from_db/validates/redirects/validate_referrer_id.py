from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE referrer_id = %s
"""


def validate_referrer_id(referrer_id):
	cur.execute(query, [referrer_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==referrer_id
