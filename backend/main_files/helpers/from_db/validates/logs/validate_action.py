from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE action = %s
"""


def validate_action(action):
	cur.execute(query, [action])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==action
