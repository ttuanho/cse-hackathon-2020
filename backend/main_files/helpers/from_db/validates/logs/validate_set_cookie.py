from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE set_cookie = %s
"""


def validate_set_cookie(set_cookie):
	cur.execute(query, [set_cookie])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==set_cookie
