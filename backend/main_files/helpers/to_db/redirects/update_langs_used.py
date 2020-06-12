from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET langs_used = %s
WHERE redirect_id = %s
"""



def update_langs_used(langs_used, redirect_id):
	cur.execute(query, [langs_used, redirect_id])
	CONNECTION.commit()
