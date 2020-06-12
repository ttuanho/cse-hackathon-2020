from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE symptoms
SET description = %s
WHERE symptom_id = %s
"""



def update_description(description, symptom_id):
	cur.execute(query, [description, symptom_id])
	CONNECTION.commit()
