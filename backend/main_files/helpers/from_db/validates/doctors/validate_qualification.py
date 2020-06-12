from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_id
FROM doctors
WHERE qualification = %s
"""


def validate_qualification_from_doctors(qualification):
	cur.execute(query, [qualification])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==qualification
