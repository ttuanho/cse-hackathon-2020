from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_id
FROM doctors
WHERE name = %s
"""


def validate_name_from_doctors(name):
	cur.execute(query, [name])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==name
