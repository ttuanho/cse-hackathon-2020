from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE html_attr = %s
"""


def validate_html_attr(html_attr):
	cur.execute(query, [html_attr])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==html_attr
