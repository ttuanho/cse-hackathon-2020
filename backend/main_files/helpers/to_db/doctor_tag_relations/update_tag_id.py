from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctor_tag_relations
SET tag_id = %s
WHERE doctor_tag_relation_id = %s
"""



def update_tag_id(tag_id, doctor_tag_relation_id):
	cur.execute(query, [tag_id, doctor_tag_relation_id])
	CONNECTION.commit()
