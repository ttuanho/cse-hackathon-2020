from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE redirect_id = %s
"""


def validate_redirect_id(redirect_id):
	cur.execute(query, [redirect_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==redirect_id
