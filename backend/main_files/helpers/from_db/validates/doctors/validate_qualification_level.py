from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_id
FROM doctors
WHERE qualification_level = %s
"""


def validate_qualification_level_from_doctors(qualification_level):
	cur.execute(query, [qualification_level])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==qualification_level
