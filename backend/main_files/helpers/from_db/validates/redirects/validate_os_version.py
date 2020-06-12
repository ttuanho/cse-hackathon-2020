from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT redirect_id
FROM redirects
WHERE os_version = %s
"""


def validate_os_version(os_version):
	cur.execute(query, [os_version])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==os_version
