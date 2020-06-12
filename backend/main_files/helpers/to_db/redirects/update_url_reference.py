from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET url_reference = %s
WHERE redirect_id = %s
"""



def update_url_reference(url_reference, redirect_id):
	cur.execute(query, [url_reference, redirect_id])
	CONNECTION.commit()
