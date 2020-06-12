from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET languages_used = %s
WHERE redirect_id = %s
"""



def update_languages_used(languages_used, redirect_id):
	cur.execute(query, [languages_used, redirect_id])
	CONNECTION.commit()
