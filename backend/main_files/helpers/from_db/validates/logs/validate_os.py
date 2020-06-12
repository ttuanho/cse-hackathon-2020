from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE os = %s
"""


def validate_os(os):
	cur.execute(query, [os])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==os
