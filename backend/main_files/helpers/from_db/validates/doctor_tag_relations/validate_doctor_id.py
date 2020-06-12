from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_tag_relation_id
FROM doctor_tag_relations
WHERE doctor_id = %s
"""


def validate_doctor_id_from_doctor_tag_relations(doctor_id):
	cur.execute(query, [doctor_id])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==doctor_id
