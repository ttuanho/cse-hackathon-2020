from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE symptom_tag_relations
SET symptom_id = %s
WHERE symptom_tag_relation_id = %s
"""



def update_symptom_id(symptom_id, symptom_tag_relation_id):
	cur.execute(query, [symptom_id, symptom_tag_relation_id])
	CONNECTION.commit()
