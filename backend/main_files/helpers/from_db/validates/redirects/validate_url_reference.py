from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE url_reference = %s
"""


def validate_url_reference(url_reference):
	cur.execute(query, [url_reference])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==url_reference
