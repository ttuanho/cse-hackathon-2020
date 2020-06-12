from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE access_time = %s
"""


def validate_access_time(access_time):
	cur.execute(query, [access_time])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==access_time
