from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctor_tag_relations
SET doctor_id = %s
WHERE doctor_tag_relation_id = %s
"""



def update_doctor_id(doctor_id, doctor_tag_relation_id):
	cur.execute(query, [doctor_id, doctor_tag_relation_id])
	CONNECTION.commit()
