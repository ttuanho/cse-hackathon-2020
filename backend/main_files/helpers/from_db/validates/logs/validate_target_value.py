from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE target_value = %s
"""


def validate_target_value(target_value):
	cur.execute(query, [target_value])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==target_value
