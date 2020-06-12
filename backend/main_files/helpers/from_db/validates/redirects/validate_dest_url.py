from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE dest_url = %s
"""


def validate_dest_url(dest_url):
	cur.execute(query, [dest_url])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==dest_url
