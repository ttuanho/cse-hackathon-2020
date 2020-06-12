from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE browser_used = %s
"""


def validate_browser_used(browser_used):
	cur.execute(query, [browser_used])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==browser_used
