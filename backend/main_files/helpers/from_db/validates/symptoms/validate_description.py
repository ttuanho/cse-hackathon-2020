from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT symptom_id
FROM symptoms
WHERE description = %s
"""


def validate_description_from_symptoms(description):
	cur.execute(query, [description])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==description
