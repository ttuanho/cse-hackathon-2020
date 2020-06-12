from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT tag_id
FROM tags
WHERE tag_name = %s
"""


def validate_tag_name_from_tags(tag_name):
	cur.execute(query, [tag_name])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==tag_name
