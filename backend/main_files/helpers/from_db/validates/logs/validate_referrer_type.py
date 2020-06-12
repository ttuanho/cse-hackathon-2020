from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE referrer_type = %s
"""


def validate_referrer_type(referrer_type):
	cur.execute(query, [referrer_type])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==referrer_type
