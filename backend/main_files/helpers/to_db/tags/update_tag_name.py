from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE tags
SET tag_name = %s
WHERE tag_id = %s
"""



def update_tag_name(tag_name, tag_id):
	cur.execute(query, [tag_name, tag_id])
	CONNECTION.commit()
