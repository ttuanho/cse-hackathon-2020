from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_tag_relation_id
FROM doctor_tag_relations
WHERE tag_id = %s
"""


def validate_tag_id_from_doctor_tag_relations(tag_id):
	cur.execute(query, [tag_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==tag_id
