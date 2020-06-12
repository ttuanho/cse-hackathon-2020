from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE curr_url = %s
"""


def validate_curr_url(curr_url):
	cur.execute(query, [curr_url])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==curr_url
