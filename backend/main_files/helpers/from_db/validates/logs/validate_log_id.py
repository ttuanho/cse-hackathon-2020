from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE log_id = %s
"""


def validate_log_id(log_id):
	cur.execute(query, [log_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==log_id
