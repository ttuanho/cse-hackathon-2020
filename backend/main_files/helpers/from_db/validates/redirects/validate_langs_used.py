from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE langs_used = %s
"""


def validate_langs_used(langs_used):
	cur.execute(query, [langs_used])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==langs_used
