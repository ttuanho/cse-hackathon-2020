from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET html_attr = %s
WHERE log_id = %s
"""



def update_html_attr(html_attr, log_id):
	cur.execute(query, [html_attr, log_id])
	CONNECTION.commit()
