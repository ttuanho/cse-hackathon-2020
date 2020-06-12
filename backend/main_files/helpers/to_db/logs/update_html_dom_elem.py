from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET html_dom_elem = %s
WHERE log_id = %s
"""



def update_html_dom_elem(html_dom_elem, log_id):
	cur.execute(query, [html_dom_elem, log_id])
	CONNECTION.commit()
