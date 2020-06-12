from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT symptom_tag_relation_id
FROM symptom_tag_relations
WHERE symptom_id = %s
"""


def validate_symptom_id_from_symptom_tag_relations(symptom_id):
	cur.execute(query, [symptom_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==symptom_id
