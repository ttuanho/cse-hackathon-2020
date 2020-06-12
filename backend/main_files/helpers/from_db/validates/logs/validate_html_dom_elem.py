from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE html_dom_elem = %s
"""


def validate_html_dom_elem(html_dom_elem):
	cur.execute(query, [html_dom_elem])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==html_dom_elem
