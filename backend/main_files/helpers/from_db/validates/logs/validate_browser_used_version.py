from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE browser_used_version = %s
"""


def validate_browser_used_version(browser_used_version):
	cur.execute(query, [browser_used_version])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==browser_used_version
